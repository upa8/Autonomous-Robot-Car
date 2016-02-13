# Function to measure the Distance of obstacel on left side
def MeasureLeft():
  
  return 100

# Function to measure the Distance of obstacel on Right side
def MeasureRight():
  
  return 100

    

def Forward():
  
  print "Forward"
            
  return 0

def Back():
            
  print "Backward"
  
  return 0

def Left():
  
  print "Left"
            
  return 0

def Right():
            
  print "Right"

  return 0

def Stop():
  
  print "Stop"
            
  return 0

def ForwardSlow():
  
  print "ForwardSlow"   
 
  return 0

def LeftSlow():
  
  print "Left Slow"
            
  return 0
def RightSlow():
  
  print "Right slow"
            
  return 0

# main code Starts here

import time              # library for accesing time
import math

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
        
        Forward()
    
    if x == 6:
        
        Right()
    
    if x == 4:
        
        Left()
            
    if x == 2:
        
        Back()
    
    if x == 5:
        
        Stop()
    
