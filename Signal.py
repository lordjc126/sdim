#import RPi.GPIO as GPIO                 
import time
import pigpio

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#GPIO.setup(17, GPIO.OUT)

#pwm = GPIO.PWM(17,50)
#pwm.start(0)
#GPIO.output(17,GPIO.LOW)

pi = pigpio.pi()
pi.set_mode(17,pigpio.OUTPUT)
pi.write(17,0)
#pi.set_PWM_frequency(17,50)
#pi.set_PWM_dutycycle(17,255)2



while True:
    print('Type an order: ')
    order = input()
    #pi.write(17,1)
    #time.sleep(1)
    #pi.write(17,0)
    #time.sleep(1)

    if order == '1':#DLDLDDLD
        st = time.time()
        time.sleep(0.01)
        pi.write(17,1)
        time.sleep(0.01)
        pi.write(17,0)
        time.sleep(0.01)
        pi.write(17,1)
        time.sleep(0.01)
        pi.write(17,0)
        time.sleep(0.02)
        pi.write(17,1)
        time.sleep(0.01)
        pi.write(17,0)
        time.sleep(0.01)
        et = time.time()
        print(et-st)
        
    if order == '2':#LDLDLDLD
        st = time.time()
        for i in range(0,4):
            pi.write(17,1)
            time.sleep(0.01)
            pi.write(17,0)
            time.sleep(0.01)
        et = time.time()
        print(et-st)
        
    if order == '3':#LLDDDLLD
        st = time.time()
        pi.write(17,1)
        time.sleep(0.02)
        pi.write(17,0)
        time.sleep(0.03)
        pi.write(17,1)
        time.sleep(0.02)
        pi.write(17,0)
        time.sleep(0.01)
        et = time.time()
        print(et-st)
        
    if order == '0':
        pi.write(17,1)
        time.sleep(0.02)
        pi.write(17,0)
        time.sleep(0.1)
        break;
    
pi.stop()     
#GPIO.cleanup()
#pwm.stop()

            