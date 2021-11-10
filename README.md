First assignment
================================
I'm Davide Bruzzo and this is my solution for the first Reasearch Track I assignment.

# Table of contents
****************************
Here down below how it is organized this README.md :

1. [Introduction](#Introduction)
2. [My solution] (#Paragraph1)
3. [Flowchart of the code] (#Paragraph2)
4. [Issues found and how I solved them] (#Paragraph3)

## Introduction <a name="Introduction"></a>
-----------------------------
Here some informations about the Robot.

#### *Installing and running* 
-----------------------------
 
The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/), [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).
Once the dependencies are installed, simply run the `test.py` script to test out the simulator.

When done, you can run the program with:

```bash
$ python run.py assignment.py
```
Or if it doesn't work you can type:


```bash
$ python2 run.py assignment.py
```
#### *Robot API*
---------

The API for controlling a simulated robot is designed to be as similar as possible to the [SR API][sr-api].

## My solution <a name="Paragraph1"></a>
------------------------------------------------

#### *How i have organized the code* 

I tried to make the flow of code as clear as possibile by dividing it in three main functions :

- moveRobot()
- moveRobotTowardsSilverBlock()
- avoidWalls()

The ```moveRobot()``` function is the one that deals with calling the other two functions. This function is cycled in a while infinite loop. 
First of all, it checks if we are closer to a silver block, so close that there is nothing between robot and the silver block.

If this is the case, ```moveRobot()``` calls ```moveRobotTowardsSilverBlock()```. This is a function to align (by rotating) and drive towards the silver block. If Robot is so close that it is under a certain distance, it can grab the block, by using the Robot class function ```R.grab()```. Then the Robot rotates handling the block and releases it, by using the Robot class function ```R.release()``` on his back. Finally it turns back to drive in counter-wise direction.  

If Robot is not near a silver block,  ```moveRobot()``` calls ```avoidWalls()``` that is a function that checks if Robot is closer to golden blocks (walls). ```avoidWalls()``` checks if Robot is in an angle and decides if it has to turn right or left, by comparing the distance from golden blocks in the two directions (right and left). The one that is bigger has more space to drive by, so this will be the side that has no wall.  ```avoidWalls()``` turns the Robot until we are far enough from walls.  
At the end, whith the two function called, or equally if there is enough space in front, the Robot can drive straight.  

*As well as we are in a while loop all this procedure is cycled costantly.*

## Flowchart of the code <a name="Paragraph2"></a>

<p align="center">
<img src="https://github.com/davidebruzzo/ResTrack/blob/main/Flowchart.drawio.png" width="900" />
<p>

