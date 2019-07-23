import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to image')
args = vars (ap.parse_args())

# read the image and conver to grayscale
image = cv2.imread (args['image'])
grayScale = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur (grayScale, (5, 5), 0)
cv2.imshow ('Image', blurred)
cv2.waitKey (0)

thresh = cv2.adaptiveThreshold (blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow ("Mean Thresh", thresh)
cv2.waitKey (0)