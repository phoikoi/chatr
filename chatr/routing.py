from channels.routing import route
channel_routing = [
    route('ticktock', 'base.consumers.ticktock'),
    ]
