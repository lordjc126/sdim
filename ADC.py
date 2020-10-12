#!/usr/bin/env python
#by shumeipai.net
import pcf8591 as ADC
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)              

GPIO.setup(17, GPIO.OUT)

pwm = GPIO.PWM(17,80)

pwm.start(0)


def setup():
    ADC.setup(0x48)

def loop():
    count = 0
    while True:
        voiceValue = ADC.read(0)
        if voiceValue:
            print 'Value:', voiceValue
            if voiceValue > 30:
                print "Voice detected! ", count
                count += 1
                GPIO.output(17,GPIO.HIGH)
            if voiceValue < 30:
                GPIO.output(17,GPIO.LOW)
            time.sleep(0.2)
            

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt: 
        pass
