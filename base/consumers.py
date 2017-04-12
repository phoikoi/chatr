from .signals import TickTock
from .utils import ClockWatcher
import sys

def ticktock(message):
    TickTock.send(None)
