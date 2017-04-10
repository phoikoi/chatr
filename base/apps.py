from django.apps import AppConfig
from base.signals import TickTock
from base.utils import yell

class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        from base.models import run_clock_listeners
        yell("base.apps.ready: connecting TickTock signal to run_clock_listeners")
        TickTock.connect(run_clock_listeners)
