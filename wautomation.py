import threading
import time, sys, termios, tty, os
import RPi.GPIO as GPIO


litrePerCount=0.1           #change this as needed for your flow sensor.
relayPin = 11               #The pin that controls the Pump Relay
flowSensorPin = 16          #The signal pin from the flow sensor

button_delay = 1

global count
count = 0


#Function for checking what key is pressed
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

#Turns on the pump relay
def relayOn():
    print("")
    print("Turning Pump Relay ON")
    GPIO.output(relayPin, GPIO.HIGH)

#Turns off the pump relay
def relayOff():
    print("")
    print("Turning Pump Relay OFF")
    GPIO.output(relayPin, GPIO.LOW)

#Function that is called each time a pulse is detected from the flow sensor
def countPulse(channel):
    global count
    count = count+1
    volume = count * litrePerCount
#    print("Count: {0}  Volume: {1}".format(count,volume), end='\r', flush=True)
    

#setup GPIO 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relayPin, GPIO.OUT)                                  
GPIO.setup(flowSensorPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
relayOff()
print("echo at p1")

GPIO.add_event_detect(flowSensorPin, GPIO.FALLING, callback=countPulse)

#print("Water Automation Pump and Flow Test v1")
#print(" Commands:")
#print(" O Turn pump ON")
#print(" F Turn pump OFF")
#print(" R Reset counter")
#print(" X Exit")
#
#while True:
#    char = getch()
# 
#    if(char == 'o'):
#        relayOn()
#        time.sleep(button_delay)
#    
#    elif(char == 'f'):
#        relayOff()
#        time.sleep(button_delay)
#        
#    elif(char == 'r'):
#        print("")
#        print("Counter Reset")
#        count=0
#        time.sleep(button_delay)
#
#    elif(char == 'x'):
#        print("")
#        print("Exit")
#        GPIO.cleanup()
#        exit(0)


