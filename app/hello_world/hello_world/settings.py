
import socket

if socket.gethostname()=="DESKTOP-G87VIM5":
    from .config.local_settings import *
else:
    from .config.docker_settings import *
