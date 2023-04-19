
import socket

if socket.gethostname()=="DESKTOP-G87VIM5":
    from .config.dev_settings import *
else:
    from .config.prod_settings import *
