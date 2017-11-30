from channels.routing import route_class
from .consumers import Demultiplexer

channel_routing = [
    route_class(Demultiplexer, path=r"^/status/")
]