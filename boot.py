print("--boot.py")
import network

from secrets import ssid, password
from setup import TURN_ON_WIFI

def do_connect():
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)
  print(wlan.scan())
  if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect(ssid, password)
    while not wlan.isconnected():
      pass
  print('network config:', wlan.ifconfig())

if TURN_ON_WIFI:
  do_connect()