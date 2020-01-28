import pyenv_wsio
import time


ws = pyenv_wsio.Client()


def namespaceConnect(nsp):
    print 'namespace', nsp.name
    nsp.send(123456,'sendString')
    # nsp.emit('aaaaaa', {'pop': 0000}, callback=emitAck)
    # nsp.emit('bbbbbb',678967)

def emitAck(stri,num,obj):
  print 'emitAck'
  print stri
  print num
  print obj
  pass

def on_cccccc(num,stri):
  print 'on_cccccc'
  print num
  print stri
  pass

def on_dddddd(num,stri,ack):
  print 'on_dddddd'
  print num
  print stri
  ack('retAck',900000)


rootNsp= ws.of('/')
rootNsp.on('connect', namespaceConnect)
rootNsp.on('cccccc',on_cccccc)
rootNsp.on('dddddd',on_dddddd)

ws.of('/admin').on('connect', namespaceConnect)

ws.connect('ws://localhost:12000/admin', headers=["userid:from_python"])

# rootNsp.emit('aaaaaa', 'abc', 456, {'pop': 0000}, callback=emitAck)
# rootNsp.emit('aaaaaa', 'abc', callback=emitAck)
# rootNsp.emit('aaaaaa', callback=emitAck)


print ws.sid
# emit=pyenv_wsio.EventEmitter()

# def aaaa(arg1,arg2):
#   print arg1,arg2

# emit.on("opened",aaaa)

# emit.emit("opened",u"a123",890)

# print "wait ws Connect"

# time.sleep(20)

# ws.close()

while(True):
    #   # print ws.recv()
    pass
# # print ws.recv()
