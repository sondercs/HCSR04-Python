import utime
from machine import Pin

trigger = Pin(14, Pin.OUT)
echo = Pin(13, Pin.IN)

while True:
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(2)
    trigger.low()
    while echo.value()==0:
        signal_off = utime.ticks_us()
    while echo.value()==1:
        signal_on = utime.ticks_us()

    timepassed = signal_on - signal_off
    dist = (timepassed * 0.0340902) / 2
    print(dist)

'''
To Workwi use this diagram
{
  "version": 1,
  "author": "Anonymous maker",
  "editor": "wokwi",
  "parts": [
    {
      "type": "wokwi-pi-pico",
      "id": "pico",
      "top": -127.95,
      "left": 42,
      "attrs": { "env": "micropython-20231227-v1.22.0" }
    },
    {
      "type": "wokwi-led-bar-graph",
      "id": "bargraph1",
      "top": 14.4,
      "left": -110.4,
      "attrs": { "color": "lime" }
    },
    {
      "type": "wokwi-hc-sr04",
      "id": "ultrasonic1",
      "top": -123.3,
      "left": -186.5,
      "attrs": { "distance": "400" }
    }
  ],
  "connections": [
    [
      "ultrasonic1:TRIG",
      "pico:GP14",
      "blue",
      [ "v19.2", "h-106", "v-134.4", "h220.8", "v201.6" ]
    ],
    [
      "ultrasonic1:ECHO",
      "pico:GP13",
      "green",
      [ "v28.8", "h-125.6", "v-153.6", "h240", "v201.6" ]
    ],
    [
      "ultrasonic1:GND",
      "pico:GND.4",
      "black",
      [ "v38.4", "h-145.2", "v-172.8", "h249.6", "v0", "h9.6", "v211.2" ]
    ],
    [
      "ultrasonic1:VCC",
      "pico:VBUS",
      "red",
      [ "v9.6", "h-86.4", "v-115.2", "h201.6", "v220.8", "h163.2", "v-201.6" ]
    ]
  ],
  "dependencies": {}
}
'''