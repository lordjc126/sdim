import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

IN1 = 12
IN2 = 11
IN3 = 13
IN4 = 15

ENA = 31
ENB = 32

GPIO.setmode(GPIO.BOARD)
GPIO.setup([IN1,IN2,IN3,IN4, ENA, ENB], GPIO.OUT)

print( "Enter speed")
x = int(input())
print("Enter direction")
y = int(input())

pwm1 = GPIO.PWM(ENA, 50)
pwm2 = GPIO.PWM(ENB, 50)

pwm1.start(0)
pwm2.start(0)

GPIO.output(IN1,GPIO.LOW)
GPIO.output(IN2,GPIO.LOW)
GPIO.output(IN3,GPIO.LOW)
GPIO.output(IN4,GPIO.LOW)

if y == 1:
    for i in range(x):
        pwm1.ChangeDutyCycle(i)
        pwm2.ChangeDutyCycle(i)
        GPIO.output(IN1,GPIO.HIGH)
        GPIO.output(IN2,GPIO.LOW)
        GPIO.output(IN3,GPIO.HIGH)
        GPIO.output(IN4,GPIO.LOW)
        if i == x-1:
            time.sleep(5)
            print (i)
        else:
            time.sleep(0.1)
            print (i)
elif y == 0:
    for i in range(x):
        pwm1.ChangeDutyCycle(i)
        pwm2.ChangeDutyCycle(i)
        GPIO.output(IN1,GPIO.LOW)
        GPIO.output(IN2,GPIO.HIGH)
        GPIO.output(IN3,GPIO.LOW)
        GPIO.output(IN4,GPIO.HIGH)
        if i == x-1:
            time.sleep(5)
            print (i)
        else:
            time.sleep(0.1)
            print (i)


GPIO.output([IN1, IN2, IN3, IN4], GPIO.LOW)

GPIO.cleanup()
pwm1.stop()
pwm2.stop()

              
#except KeyboardInterrupt:
#    GPIO.cleanup()