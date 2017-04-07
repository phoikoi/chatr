from configparser import RawConfigParser

class _CONFIG_WRAPPER:
    CONFIG = None

def load_config(path):
    config_file = RawConfigParser()
    config_file.read(path)
    config = {}
    for x in config_file:
        for y in config_file[x].items():
            config["{}.{}".format(x,y[0])] = y[1]
    _CONFIG_WRAPPER.CONFIG = config
    return config

def config(key, default=None):
    try:
        return _CONFIG_WRAPPER.CONFIG[key]
    except KeyError:
        return default

def config_int(*args, **kwargs):
    return int(config(*args, **kwargs))

def config_bool(*args, **kwargs):
    val = config(*args, **kwargs)
    if val is None:
        return None
    if val.upper() in ['YES','TRUE','YEAH', 'SURE', 'YUP', 'SI', 'OUI', 'JA', 'ON']:
        return True
    if val.upper() in ['NO','FALSE','NAH', 'MEH', 'NOPE','NON','NEIN', 'OFF']:
        return False
    try:
        if int(val) != 0:
            return True
    except:
        pass
    return False

def config_list(*args, **kwargs):
    return [x.strip() for x in config(*args, **kwargs).split(',')]
