import sys
from django.conf import settings
from django.utils.timezone import now
from functools import wraps
from base.signals import TickTock
from uuid import uuid4
from pydoc import locate
from croniter import croniter
from datetime import datetime

namestr = lambda x:f"{x.__module__}.{x.__name__}"

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
    yell("Entering clocklistener")
    def decorator(func):
        yell("Entering decorator")
        _basetime = now()
#        @wraps(func)
        def wrapper(**kwargs):
            yell("Entering wrapper")
            nonlocal cron_spec
            nonlocal _basetime
            yell(f"wrapper: nonlocal _cronspec is {cron_spec}")
            yell(f"wrapper: nonlocal _basetime is {str(_basetime)}")
            next_run = croniter(cron_spec, _basetime).get_next(datetime)
            yell(f"wrapper: next_run is {str(next_run)}")
            curtime = now()
            if next_run <= curtime:
                _basetime = curtime
                yell(f"About to execute func {namestr(func)}")
                return func()
            else:
                yell(f"Not executing func {namestr(func)}")
                return None
        yell(f"About to connect TickTock for {namestr(func)}")
        TickTock.connect(wrapper, dispatch_uid=namestr(func))
        yell("About to return wrapper")
        return wrapper
    yell("About to return decorator")
    return decorator
