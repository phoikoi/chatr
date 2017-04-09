from django.apps import AppConfig
from base.signals import TickTock
from base.models import run_clock_listeners

class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        TickTock.connect(run_clock_listeners)
