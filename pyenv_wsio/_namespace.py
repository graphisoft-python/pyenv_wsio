# # -*- coding: utf-8 -*-

from ._events import EventEmitter


class ClientNamespace(EventEmitter):
    def __init__(self, name, client):
        EventEmitter.__init__(self)
        self.conn = client
        self.name = name
        self.connected=False

    def connect(self):
      pass

    def disconnect(self):
      pass

    def emit(self):
      pass

    def onevent(self,pkg):
      pass
