
#!/usr/bin//env python
# -*- coding:utf-8 -*-
import smbus   
import time
 
address = 0x48 ## address  ---> 
A0 = 0x40      ##  A0    ----> 
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1) 
while True: 
    bus.write_byte(address,A1)  
    value = 143-bus.read_byte(address) 
    print("light:%1.0f " %(value)) 
    time.sleep(1) 
