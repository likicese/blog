#!/usr/bin/python3
import sys
import Adafruit_DHT
import datetime

while True:
        humidity,temperature = Adafruit_DHT.read_retry(11, 26)
            x = datetime.datetime.now()
                print ('Date: {0} Temp: {1:0.1f} C Humidity: {2:0.1f} %'.format(x, temperature, humidity))
