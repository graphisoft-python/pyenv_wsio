import pyenv_wsio
import time


ws=pyenv_wsio.WebSocketIO()


def onOpened():
  print "wsOpened"

def onClosed():
  print "wsClosed"
  cntWs()

def onMessage(data):
  print "wsMessage",data

def onError():
  print "wsError"

ws.on("open",onOpened)
ws.on("close",onClosed)
ws.on("message",onMessage)
ws.on("error",onError)

def cntWs():
  ws.connect('ws://localhost:8080/ws-accept',header=["userid:from_python"],timeout=1000)

cntWs() 
# emit=pyenv_wsio.EventEmitter()

# def aaaa(arg1,arg2):
#   print arg1,arg2

# emit.on("opened",aaaa)

# emit.emit("opened",u"a123",890)

print "wait ws Connect"

time.sleep(20)

ws.close()

while(True):
#   # print ws.recv()
  pass
# # print ws.recv()