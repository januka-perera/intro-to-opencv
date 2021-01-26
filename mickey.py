"""
Displaying Things
Now, perhaps we want to not only show our image, but also highlight a certain portion of it. OpenCV provides 
a number of functions for doing that. Let's take a look at some:
"""

import numpy as np # Numpy is a numerical library in python. OpenCV is based in numpy and hence when doing low level operations we need numpy in our code.
import cv2

canvas = np.zeros((600,600,3),np.uint8) # Create a blank, black canvas to draw on.

WHITE = (255,255,255) # Colour (B,G,R)

cv2.circle(canvas, (300,300),150,WHITE,-3) # Face
cv2.circle(canvas,(170,170), 70, WHITE, -3) # Left ear
cv2.circle(canvas,(430,170), 70, WHITE, -3) # Right ear

cv2.imshow("result",canvas)
cv2.waitKey(-1)

#### Exercises ####
# 1. Try to draw a disney Mickey Mouse logo (a few circles) with openCV. Make it white on black.
# Think about how you can use the cv2.circle command to help ease the process. Have your window be a 600x600 size.
# 2. Now try to draw the logo black on white instead of white on black.
# 3. Draw an even more complex image using polygons and lines, and send us the image!
# 4. [CHALLENGE] Use the polylines function to draw a sine wave on a canvas.
# 5. [CHALLENGE] Make a little bouncing ball animation and save it to an mp4 file. This stackoverflow post might help:
# https://stackoverflow.com/questions/30509573/writing-an-mp4-video-using-python-opencv
