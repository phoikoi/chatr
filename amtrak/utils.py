from base.utils import clocklistener, yell
import sys

@clocklistener('*/5 * * * *')
def clock_tick():
    yell('clock_tick running')
