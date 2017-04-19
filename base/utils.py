import sys
from django.conf import settings
from django.utils.timezone import now
from functools import wraps
from base.signals import TickTock
from uuid import uuid4
from pydoc import locate
from croniter import croniter
from datetime import datetime

def yell(message):
    if settings.DEBUG:
        t = now().strftime('%Y%m%d_%H%M%S_%Z')
        sys.stdout.write(f'{t}: {message}\n')
        sys.stdout.flush()

# From http://stackoverflow.com/a/13653312
def fullname(o):
    module = o.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return o.__class__.__name__
    return module + '.' + o.__class__.__name__

def clocklistener(cron_spec):
    _cronspec = cron_spec
    _basetime = now()
    yell(f"Entering clocklistener: cronspec _basetime")
    def decorator(func):
        yell("Entering decorator")
#        @wraps(func)
        def wrapper(**kwargs):
            yell("Entering wrapper")
            nonlocal _cronspec
            nonlocal _basetime
            yell(f"wrapper: nonlocal _cronspec is {_cronspec}")
            yell(f"wrapper: nonlocal _basetime is {str(_basetime)}")
            next_run = croniter(_cronspec, _basetime).get_next(datetime)
            yell(f"wrapper: next_run is {str(next_run)}")
            curtime = now()
            if next_run <= curtime:
                _basetime = curtime
                yell("About to execute func {fullname(func)}")
                return func()
            else:
                yell("Not executing func")
                return None
        yell("About to connect TickTock for {fullname(func)}")
        TickTock.connect(wrapper, dispatch_uid=fullname(func))
        yell("About to return wrapper")
        return wrapper
    yell("About to return decorator")
    return decorator
