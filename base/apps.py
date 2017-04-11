from django.apps import AppConfig
from base.signals import TickTock

class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        from base.models import run_clock_listeners
        TickTock.connect(run_clock_listeners, dispatch_uid='ticktock_signal')
