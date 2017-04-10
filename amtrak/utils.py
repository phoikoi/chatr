import sys
from django.utils.timezone import now
from base.utils import yell

def clock_tick():
    yell(f"{str(now())}")
