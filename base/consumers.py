from .signals import TickTock
from .utils import ClockWatcher, yell
import sys

def ticktock(message):
    yell("base.consumers.ticktock: sending TickTock signal")
    TickTock.send(ClockWatcher)
