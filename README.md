First assignment
================================
I'm Davide Bruzzo and this is my solution for the first Reasearch Track I assignment. The request of the assignment was to write a python script for achieving this robot’s behaviour:

- constantly drive the robot around the circuit in the counter-clockwise direction
- avoid touching the golden boxes
- when the robot is close to a silver box, it should grab it, and move it behind itself

# Table of contents
****************************
Here down below how it is organized this README.md :

1. [Introduction](#introduction)
2. [My solution](#solution)
3. [Flowchart of the code](#flowchart)
4. [Video demonstration](#video)
5. [Final considerations and conclusions](#issues)

## Introduction <a name="introduction"></a>
-----------------------------

#### *Installing and running* 
-----------------------------
 
The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/), [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).


When done, you can run the program with:

```bash
$ python run.py assignment.py
```
Or if it doesn't work you can type:


```bash
$ python2 run.py assignment.py
```

# My solution <a name="solution"></a>
------------------------------------------------

#### *How I have organized the code* 

I tried to make the flow of code as clear as possibile by dividing it in three main functions :

- moveRobot()
- moveRobotTowardsSilverBlock()
- avoidWalls()

The ```moveRobot()``` function is the one that deals with calling the other two functions. This function is cycled in a while infinite loop. 
First of all, it checks if we are closer to a silver block, so close that there is nothing between robot and the silver block.

If this is the case, ```moveRobot()``` calls ```moveRobotTowardsSilverBlock()```. This is a function to align (by rotating) and drive towards the silver block. If Robot is so close that it is under a certain distance, it can grab the block, by using the Robot class function ```R.grab()```. Then the Robot rotates handling the block and releases it, by using the Robot class function ```R.release()``` on his back. Finally it moves a bit away and turns back to drive in counter-wise direction.  

If Robot is not near a silver block,  ```moveRobot()``` calls ```avoidWalls()``` that is a function that checks if Robot is closer to golden blocks (walls). ```avoidWalls()``` checks if Robot is in an angle and decides if it has to turn right or left, by comparing the distance from golden blocks in the two directions (right and left). The one that is bigger has more space to drive by, so this will be the side that has no wall.  ```avoidWalls()``` turns the Robot until we are far enough from walls.  
At the end, whith the two function called, or equally if there is enough space in front, the Robot can drive straight.  

***As well as we are in a while loop all this procedure is cycled costantly.***

# Flowchart of the code <a name="flowchart"></a>

<p align="center">
<img src="https://github.com/davidebruzzo/ResTrack/blob/main/Flowchart.drawio.png" width="900" />
<p>

 # Video demonstration <a name="video"></a>
------------------------------------------------  
 This is a demo, here the robot makes three laps in counter-clockwise direction in the arena:
 [![](https://img.youtube.com/vi/a6Pq5laFK8o/0.jpg)](https://www.youtube.com/watch?v=a6Pq5laFK8o)
 
 # Final considerations and conclusions <a name="issues"></a>
------------------------------------------------

 Dealing with solving the problem I found some solutions that helped me to achieve some tasks.  
 First of all, I reduced the angle of visibility of the robot in order to be more sure that the robot was facing walls and they were not by its sides.  
 Also reducing the working range of seeing silver blocks helped me to detect this block only when they are very close and there's nothing in between.  
 To make the robot turn in the right direction choosing between right and left, I had to select the nearest block on left and nearest one on rigth. By this two distances it decides where to turn based on how much free space there is.  
 Last code improvement was trying to speed up the velocity of the robot by driving faster. This required a reduction in time of driving in order to have more rapid checks.
 
 
