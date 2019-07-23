import numpy as np
import cv2
import imutils
import argparse

# set up the image args
ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to the image')
args = vars (ap.parse_args())

# read the image
image = cv2.imread (args['image'])

# rotate the image by calling the function in imutils
rotated_image = imutils.rotate_image (image, 180)

cv2.imshow ('Rotated image', rotated_image)
cv2.waitKey(0)