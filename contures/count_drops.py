# In order to find the contures in an image, you need to first obtain a binarization of the image,
# using either edge detection methods of thresholding.
import cv2
import argparse
import numpy as np

# handle the args
ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to the image')
args = vars (ap.parse_args())

# read and convert image to GRAYSCALE
image = cv2.imread (args['image'])
grayScaleImage = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur (grayScaleImage, (11, 11), 0)
cv2.imshow ('Graussian Blurred image', blurred)

# now apply canny edge detection metod
cannyEdge = cv2.Canny (blurred, 30, 150)
cv2.imshow ('Canny Edge Detection', cannyEdge)

# find the contures
cnts, hierarchy = cv2.findContours(cannyEdge.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

rounds = image.copy()
cv2.drawContours (rounds, cnts, -1, (0, 255, 0), 2)
cv2.imshow ('Contours', rounds)
cv2.waitKey(0)