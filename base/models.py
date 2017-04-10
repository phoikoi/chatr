from django.db import models
from django.utils.timezone import now
from pydoc import locate
from croniter import croniter
from datetime import datetime
from base.utils import yell

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ClockListener(BaseModel):
    cron_spec = models.CharField(max_length=128)
    last_run = models.DateTimeField(auto_now_add=True)
    target_object = models.CharField(max_length=128)

    @property
    def next_run(self):
        return croniter(self.cron_spec, self.last_run).get_next(datetime)

    def run(self):
        self.last_run = now()
        self.save()
        yell(f"ClockListener {self.id} \"{self.cron_spec}\" {self.target_object} in run()")
        locate(self.target_object)()

def run_clock_listeners(**kwargs):
    nowtime = now()
    q = ClockListener.objects.all()
    listeners = [x for x in q if x.next_run<=now()]
    for x in listeners:
        x.run()
