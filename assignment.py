from __future__ import print_function

import time
from sr.robot import *

"""
Assignment code

"""

"""
Distance and angle to go towards silver block
"""
d_th = 0.4
a_th = 2.0

R = Robot()
""" instance of the class Robot"""

def drive(speed, seconds):
    """
    Function for setting a linear velocity

    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

#here goes the code

def findMarkerGold():

	""" 
	function to find marker gold 
	
	"""

	dist = 100
	 	
 	for marker in R.see():
 	 	if marker.dist < dist and marker.info.marker_type is MARKER_TOKEN_GOLD and -45 < marker.rot_y < 45:
 	 		dist = marker.dist
	        	rot_y = marker.rot_y
	        	typeMarker = marker.info.marker_type
	if dist==100:
	          return -1, -1
	else:
	  	#print (dist, rot_y)
	        return dist, rot_y
	 
def findMarkerSilver():
	
	""" 
	function to find marker silver
	
	"""

	dist = 100
	 	
 	for marker in R.see():
 	 	if marker.dist < dist and marker.info.marker_type is MARKER_TOKEN_SILVER and  -45 < marker.rot_y < 45:
 	 		dist = marker.dist
	        	rot_y = marker.rot_y
	        	typeMarker = marker.info.marker_type
	if dist==100:
	          return -1, -1
	          print (dist, rot_y)
	else:
	 	#print (dist, rot_y)
	 	return dist, rot_y


def avoidWalls(distGold, rot_yGold):

	"""
	Function to check if we are closer to a gold block, that represents the wall
	
	Args: distGold = distance of the gold block
	      rot_yGold = angle of the gold block
	
	"""
	if distGold < 0.8:	        		
		
		#Initialization of two variables for checking angles
		distLeft = 100
		distRigth = 100
		
		#Checking if robot is in an angle and where it has to go
		print("Checking angles!\n")
 		for marker in R.see():
 		
 			if  marker.info.marker_type is MARKER_TOKEN_GOLD:
 	
 				if -100 < marker.rot_y < -60 and marker.dist < distLeft:	#Reduced angle of visibility of the robot in order to avoid errors detecting walls on sides
 					distLeft = marker.dist
	       		
				if  60 < marker.rot_y < 100 and marker.dist < distRigth:
 					distRigth = marker.dist
		
		print("Distance from left wall is: ", distLeft)
		print("Distance from rigth wall is: ", distRigth, "\n")
		print("I have to turn: \n")			
		
		if distLeft > distRigth:	# If there is more free space on left side it means that robot has to go in that direction
					
			turn(-20, 0.5)
			print("\t\tLeft!\n")
		else:				# Else: there is more space on rigth side
			turn(20, 0.5)
			print("\t\tRigth!\n")
	
	distGold, rot_yGold = findMarkerGold() # Updating gold distance and angle
	return distGold, rot_yGold
		
			
def moveRobotTowardsSilver(distSilver, rot_ySilver):	
	
	"""
	Function to move closer to a silver block, that has to be grabbed
	
	Args: distSilver = distance of the silver block
	      rot_ySilver = angle of the silver block
	
	"""		
		
	if distSilver < d_th: 	        	
	        	
		print("Grabbed the silver block!\n")
	      	R.grab() # If we are close to the token, we grab it.
	        	
	      	turn(20, 3) 
	      	R.release()
	      	print("Silver block released!\n")
	      	turn(-20,3)
	      	drive(20,0.3)
	        	        	
	elif -a_th<= rot_ySilver <= a_th: # if the robot is well aligned with the token, we go forward
	      	print("Ah, I am well aligned! Going straigth!\n")
	      	drive(40, 0.1)
	elif rot_ySilver < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
	      	print("Left a bit to align with silver block...\n")
	      	turn(-2, 0.5)
	elif rot_ySilver > a_th:
	      	print("Right a bit to align with silver block...\n")
	      	turn(+2, 0.5)

        distSilver, rot_ySilver = findMarkerSilver()	#update the silver's block info
        return distSilver, rot_ySilver
		
def moveRobot(distSilver, rot_ySilver, distGold, rot_yGold):
	
	"""
	Function to to manage the robot, it calls the other two function when it is the rigth case 
	
	Args: distGold = distance of the gold block
	      rot_yGold = angle of the gold block
	      distSilver = distance of the silver block
	      rot_ySilver = angle of the silver block
	
	"""
	if 0 < distSilver < 1.5:
		
		if 1.4 < distSilver < 1.5:
			print("Silver block detected!\n") #to show only once he found the silver block
			
		print("Distance from silver block is: ", distSilver, "\n")	# if the robot is near a silver block it shows that it is getting closer by reducing the distance
		moveRobotTowardsSilver(distSilver, rot_ySilver)
		
	else: 
		avoidWalls(distGold, rot_yGold)				# if the robot is far from a silver block, checks if there are walls and drives avoiding them
		print("Driving straight!\n")
		drive(40, 0.1)
		

def main():

	drive(40,0.5)								# start moving the robot
	
	while(1):
		distSilver, rot_ySilver = findMarkerSilver()
		distGold, rot_yGold = findMarkerGold()	
		moveRobot(distSilver, rot_ySilver, distGold, rot_yGold)
		

main()
