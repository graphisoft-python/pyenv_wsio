import pyenv_wsio
import time


ws=pyenv_wsio.Client()


def onOpened():
  print "wsOpened"

def onClosed():
  print "wsClosed"
  cntWs()

def onMessage(data):
  print "wsMessage"
  print data.packet_type
  print data.data
  print data.namespace
  print data.id
  print data.attachments

def onError(e):
  print "wsError"
  print e

ws.on("open",onOpened)
ws.on("close",onClosed)
ws.on("message",onMessage)
ws.on("error",onError)
ws.on('packet',onMessage)

def cntWs():
  ws.connect('ws://localhost:12000/admin',headers=["userid:from_python"])


cntWs() 

print ws.sid
# emit=pyenv_wsio.EventEmitter()

# def aaaa(arg1,arg2):
#   print arg1,arg2

# emit.on("opened",aaaa)

# emit.emit("opened",u"a123",890)

print "wait ws Connect"

time.sleep(20)

# ws.close()

while(True):
#   # print ws.recv()
  pass
# # print ws.recv()