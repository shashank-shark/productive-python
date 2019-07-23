import numpy as np
import argparse
import cv2
import imutils

# get the command line arguments set up
ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to image')
args = vars (ap.parse_args())

# read the image
image = cv2.imread (args['image'])

# resize the image, code is in imutils
resized_image = imutils.resize_image (image, 400, 720)

cv2.imshow ('Resized image', resized_image)
cv2.waitKey (0)