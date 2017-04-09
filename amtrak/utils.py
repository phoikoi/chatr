import sys
from django.utils.timezone import now

def clock_tick():
    sys.stdout.write(f"{str(now())}\n")
