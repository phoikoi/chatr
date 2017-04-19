from django.apps import AppConfig
from base.signals import TickTock


class AmtrakConfig(AppConfig):
    name = 'amtrak'

    def ready(self):
        import amtrak.utils # connect clocklisteners
