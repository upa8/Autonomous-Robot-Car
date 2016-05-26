# Function to measure the Distance of obstacel on left side
def MeasureLeft():
  flag=0
  print("Left Distance Measurement In Progress")
  
  GPIO.output(TRIG_L, False)
  print("Waiting For Sensor To Settle")
  time.sleep(.5)
  
  GPIO.output(TRIG_L, True)
  time.sleep(0.00001)
  GPIO.output(TRIG_L, False)
  
  while GPIO.input(ECHO_L)==0:
    pulse_start = time.time()

  while GPIO.input(ECHO_L)==1:  
    pulse_end = time.time()
  
  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150

  distance = round(distance, 2)

  if distance >200:
    distance = 0

  print("Left Distance:",distance,"cm")

  return distance

# Function to measure the Distance of obstacel on Right side
def MeasureRight():
  
  print("Right Distance Measurement In Progress")
  
  GPIO.output(TRIG_R, False)
  print("Waiting For Sensor To Settle")
  time.sleep(.5)
  
  GPIO.output(TRIG_R, True)
  time.sleep(0.00001)
  GPIO.output(TRIG_R, False)
  
  while GPIO.input(ECHO_R)==0:
    pulse_start = time.time()
 
  while GPIO.input(ECHO_R)==1:
    pulse_end = time.time()
 
  pulse_duration = pulse_end - pulse_start

  distance = pulse_duration * 17150

  distance = round(distance, 2)

  if distance >200:
    distance = 0
   
  print("Right Distance:",distance,"cm")

  return distance

    

def Forward():
  
  while TRUE:   
    checkObs()        
            
  return 0

def Back():
  
  while TRUE:   
    checkObs()        
  
  return 0

def Left():
  
  while TRUE:   
    checkObs()        

  return 0

def Right():
  
  while TRUE:   
    checkObs()        
  
  return 0

def Stop():
  
  while TRUE:   
    checkObs()        
  
  return 0

# All slow methods
def ForwardSlow():
  
  while TRUE:   
    checkObs()        
  
  return 0

def LeftSlow():
  
  while TRUE:   
    checkObs()        
            
  return 0
def RightSlow():
  
  while TRUE:   
    checkObs()        
  
            
  return 0

def BackSlow():
  
  while TRUE:   
    checkObs()        
  
  return 0

def checkObs():
  
  leftDistance = MeasureLeft()
  rightDistance = MeasureRight()

  if leftDistance < 20:

    print "Obstacle found by left"
    Stop()
    break

  if rightDistance < 20:

    print "Obstacle found by right"
    Stop()
    break


# Encoder code for distance

# main code Starts here
import RPi.GPIO as GPIO  # library for accessing GPIO
import time              # library for accesing time
import math

GPIO.setmode(GPIO.BOARD) # calling Raspi pin by pin no. on boards
GPIO.setwarnings(False)
# Setting the Pins for interfacing Hardware
#ENCODER_L = 15 
#ENCODER_R = 16

MOTOR_L1 = 21
MOTOR_L2 = 22

MOTOR_R1 = 11
MOTOR_R2 = 12

ECHO_L = 29
TRIG_L = 31

ECHO_R = 33
TRIG_R= 35

# defining the hardware type I/P or O/P
#GPIO.setup(ENCODER_L,GPIO.IN)
#GPIO.setup(ENCODER_R,GPIO.IN)

GPIO.setup(TRIG_L,GPIO.OUT)
GPIO.setup(ECHO_L,GPIO.IN)

GPIO.setup(TRIG_R,GPIO.OUT)
GPIO.setup(ECHO_R,GPIO.IN)


GPIO.setup(MOTOR_L1,GPIO.OUT)
GPIO.setup(MOTOR_L2,GPIO.OUT)
GPIO.setup(MOTOR_R1,GPIO.OUT)
GPIO.setup(MOTOR_R2,GPIO.OUT)


# main loop starts here
while True:
       
       
    Distance_Left = MeasureLeft();
    Distance_Right = MeasureRight();
    #print "Left Distance"
    #print Distance_Left 
    #print "Right Distance"
    #print Distance_Right    
    
    x = input("Please Enter something")
        
    if x == 8:
        
        ForwardSlow()
        
    if x == 6:
        
        RightSlow()

    
    if x == 4:
        
        LeftSlow()
            
    if x == 2:
        
        Back()
    
    if x == 5:
        
        Stop()
    if x == 88:

        Forward()

    if x == 66:
        
        Right()

    if x == 44:

        Left()
    
    if x == 22:

        Back()

GPIO.cleanup()
