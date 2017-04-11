from django.core.management.base import BaseCommand, CommandError
from django.utils.timezone import now
from channels import Channel
from time import sleep

class Command(BaseCommand):
    help = 'Sends a special channel message each minute for periodic tasks'

    def handle(self, *args, **options):
        try:
            while True:
                Channel('ticktock').send({'ticktock':1})
                sleep(60-(now().second))
        except KeyboardInterrupt:
            return
