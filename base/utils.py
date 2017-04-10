import sys
from django.conf import settings
from django.utils.timezone import now

class ClockWatcher:
    pass

def yell(message):
    if settings.DEBUG:
        sys.stdout.write(f"{str(now())} {message}\n")
        sys.stdout.flush()
