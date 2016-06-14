# client.py  (c) 2013 @whaleygeek
#
# A demo client that pokes "hello" at a server once per second

import network
import time

try:
	network.call("localhost")
except:
	print ("NO SERVER FOUND!")
	
while network.isConnected():
  print("sending")
  network.say("hello")
  time.sleep(1)
  
