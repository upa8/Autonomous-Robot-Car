
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
  
  GPIO.output(21,1)
  GPIO.output(22,0)
  GPIO.output(11,1)
  GPIO.output(12,0)		
			
  return 0

def Back():
  
  GPIO.output(21,0)
  GPIO.output(22,1)
  GPIO.output(11,0)
  GPIO.output(12,1)		
			

  return 0

def Left():
  
  GPIO.output(21,0)
  GPIO.output(22,0)
  GPIO.output(11,1)
  GPIO.output(12,0)		
			
  return 0

def Right():
  
  GPIO.output(21,1)
  GPIO.output(22,0)
  GPIO.output(11,0)
  GPIO.output(12,0)		
			
  return 0

def Stop():
  
  GPIO.output(21,0)
  GPIO.output(22,0)
  GPIO.output(11,0)
  GPIO.output(12,0)		
			
  return 0

def ForwardSlow():
  
  Forward()
  time.sleep(.2)
  Stop()
  time.sleep(.2)
			
  return 0

def LeftSlow():
  
  Left()
  time.sleep(.2)
  Stop()
  time.sleep(.2)
			
  return 0
def RightSlow():
  
  Right()
  time.sleep(.2)
  Stop()
  time.sleep(.2)
			
  return 0


def Distance(x):
  count_l = 0
  dist_l = 0

  count_r = 0
  dist_r = 0

  while 1:
    i=GPIO.input(ENCODER_L)
    j=GPIO.input(ENCODER_R)

    Forward()

    if i==1 and count_l == 0:
      count_l = 1

    if i==0 and count_l == 1:

      count_l = 0
      if dist_l == x and dist_r == x:
        break

      else:
        dist_l +=1
      
    if j==1 and count_r == 0:
      count_l = 1

    if j==0 and count_r == 1:
      count_r = 0

      if dist_l == x and dist_r == x:
        break

      else:
        dist_r +=1
        
  return 0


def LeftTurn(angle):
  count_r = 0
  dist_r = 0
  x = math.radians(angle)
  y = 50*math.sin(x)
  

  while 1:
    j=GPIO.input(ENCODER_R)

    Left()
    
    if j==1 and count_r == 0:
      count_l = 1

    if j==0 and count_r == 1:
      count_r = 0

      if dist_r == x:
        break

      else:
        dist_r +=1
        
  return 0


def RightTurn(angle):
  count_l = 0
  dist_l = 0
  x = math.radians(angle)
  y = 50*math.sin(x)

  while 1:
    i=GPIO.input(ENCODER_L)

    Right()
    
    if i==1 and count_l == 0:
      count_l = 1

    if i==0 and count_l == 1:
      count_l = 0

      if dist_l == x:
        break

      else:
        dist_l +=1
        
  return 0





# main code Starts here

import RPi.GPIO as GPIO  # library for accessing GPIO
import time              # library for accesing time
import serial            # library for accesing serial port
import math


GPIO.setmode(GPIO.BOARD) # calling Raspi pin by pin no. on boards
GPIO.setwarnings(False)
# Setting the Pins for interfacing Hardware
ENCODER_L = 15 
ENCODER_R = 16

MOTOR_L1 = 21
MOTOR_L2 = 22

MOTOR_R1 = 11
MOTOR_R2 = 12

ECHO_L = 29
TRIG_L = 31

ECHO_R = 33
TRIG_R= 35

# defining the hardware type I/P or O/P
GPIO.setup(ENCODER_L,GPIO.IN)
GPIO.setup(ENCODER_R,GPIO.IN)

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
       print("---------------------------")

       ser = serial.Serial ("/dev/ttyAMA0") # opening serial port
       ser.baudrate=9600        # setting baud rate 9600 bits/sec  

       Distance_Left = MeasureLeft();
       Distance_Right = MeasureRight();
#      ser.write("L",str(int(Distance_Left)),"R",str(int(Distance_Right)))
       ser.write("L")
       ser.write(str(int(Distance_Left)))

       ser.write("R")
       ser.write(str(int(Distance_Right)))

       data = ser.read(3)
	
       if data == "F00":
           Forward()
           print("Forward")
       
       elif data == "L00":
           Left()
           print("Left")

       elif data == "R00":
           Right()
           print("Right")

       elif data == "S00":
           Stop()
           print("Stop")
    

       elif data == "FF0":
           ForwardSlow()
           print("Forward Slow")
       
       elif data == "LL0":
           LeftSlow()
           print("Left Slow")

       elif data == "RR0":
           RightSlow()
           print("Right Slow")
       
       else: 
          if data[0] == 'F':
              y= 10*int(data[1]) + int(data[2])
              print("Forward _encoder:",y)
              Distance(y)
              
          elif data[0] == 'L':
              y= 10*int(data[1]) + int(data[2])
              print("Left _encoder:",y)
              LeftTurn(y)
              
          elif data[0] == 'R':
              y= 10*int(data[1]) + int(data[2])
              print("Right _encoder;",y)
              RightTurn(y)
              
              ser.close()

GPIO.cleanup()
	
