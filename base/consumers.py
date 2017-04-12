from .signals import TickTock
import sys

def ticktock(message):
    TickTock.send(None)
