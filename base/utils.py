import sys
from django.conf import settings
from django.utils.timezone import now
from functools import wraps

def yell(message):
    if settings.DEBUG:
        t = now().strftime('%Y%m%d_%H%M%S_%Z')
        sys.stdout.write(f'{t}: {message}\n')
        sys.stdout.flush()

def clocklistener(cron_spec):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator

