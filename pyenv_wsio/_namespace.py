# # -*- coding: utf-8 -*-

from ._events import EventEmitter
from . import _packet

import six
import itertools


class ClientNamespace():
    def __init__(self, name, client):
        # EventEmitter.__init__(self)
        self.emitter = EventEmitter()
        self.conn = client
        self.name = name
        self.connected = False
        self.callbacks = {0: itertools.count(1)}

    def on_connect(self):
        self.connected = True
        self.emitter.emit('connect', self)

    def on_disconnect(self):
        self.connected = False
        self.emitter.emit('disconnect', self)

    def on_ack(self, id, data):
        callback = None
        try:
            callback = self.callbacks[id]
        except KeyError:
            pass
        else:
            del self.callbacks[id]

        if callback is not None:
            callback(*data)

    def on_event(self, id, data):
        evt = data[0]
        data = data[1:]
        if id is not None:
            def __do__ack(*args):
                if isinstance(args, tuple):
                    args = list(args)
                else:
                    args = []
                self.conn._send_packet(_packet.Packet(
                    _packet.ACK, namespace=self.name, data=args, id=id))

            data.append(__do__ack)
        self.emitter.emit(evt, *data)
        pass

    def on_error(self, data):
        self.connected = False
        self.emitter.emit('error', *data)

    def on(self, event, listener):
        self.emitter.on(event, listener)

    def once(self, event, listener):
        self.emitter.once(event, listener)

    def emit(self, event, *args, **kwargs):

        if not self.connected:
            return

        callback = kwargs.pop('callback', None)
        if callback is not None:
            id = self._generate_ack_id(callback)
        else:
            id = None

        if isinstance(args, tuple):
            args = list(args)
        else:
            args = []

        self.conn._send_packet(_packet.Packet(
            _packet.EVENT, namespace=self.name, data=[event]+args, id=id))

    def send(self, *args, **kwargs):
        self.emit('message', *args, **kwargs)

    def _generate_ack_id(self, callback):
        id = six.next(self.callbacks[0])
        self.callbacks[id] = callback
        return id
