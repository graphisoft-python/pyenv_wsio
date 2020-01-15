# # -*- coding: utf-8 -*-

import signal
from ._events import EventEmitter
from ._wsio import *

reconnecting_clients = []


def _signal_handler(sig, frame):
    pass


_original_signal_handler = signal.signal(signal.SIGINT, _signal_handler)


class Client(EventEmitter):
    def __init__(self, reconnection=True, reconnection_attempts=0,
                 reconnection_delay=1, reconnection_delay_max=5,
                 randomization_factor=0.5, binary=False):
        EventEmitter.__init__(self)

        self.reconnection = reconnection
        self.reconnection_attempts = reconnection_attempts
        self.reconnection_delay = reconnection_delay
        self.reconnection_delay_max = reconnection_delay_max
        self.randomization_factor = randomization_factor
        self.binary = binary

        self.eio=Wsio()
        self.eio.on('connect',self.on_eio_connect)
        self.eio.on('message',self.on_eio_message)
        self.eio.on('disconnect',self.on_eio_disconnect)
        self.eio.on('error',self.on_eio_error)

        self.connection_url = None
        self.connection_headers = None
        self.connection_namespaces = None
        self.sid = None

        self.connected = False
        self.namespaces = []
        self.handlers = {}
        self.namespace_handlers = {}
        self.callbacks = {}
        self._binary_packet = None
        self._reconnect_task = None
        self._reconnect_abort = self.eio.create_event()


    def connect(self,url, headers={},namespaces=None):
      self.connection_url=url
      self.connection_headers=headers
      self.connection_namespaces=namespaces
      self.eio.connect(url,headers=headers)
      self.connected=True

    # def emit()
    
    def on_eio_connect(self):
      self.sid=self.eio.sid

    def on_eio_message(self,pkg):
      print 'on_eio_message'

    def on_eio_disconnect(self):
      print 'on_eio_disconnect'

    def on_eio_error(self,e):
      print 'on_eio_error'

