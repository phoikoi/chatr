from .signals import TickTock
from .utils import ClockWatcher

def ticktock(message):
    TickTock.send(ClockWatcher)
