from machine import Pin
import time


led1 = Pin(2, Pin.OUT)      # ESP32 internal pin 
led2 = Pin(23, Pin.OUT)     # ESP32 pin 23

for i in range(5):
    led1.on()
    led2.off()
    time.sleep(0.5) # seconds

    led1.off()
    led2.on()
    time.sleep(0.5) # seconds

led1.off()
led2.off()
