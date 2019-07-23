import cv2
import argparse
import numpy as np

# handle the args
ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to the image')
args = vars (ap.parse_args())

# read the image
image = cv2.imread (args['image'])
cv2.imshow ('Original Image', image)
cv2.waitKey(0)

# gray
grayImage = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
cv2.imshow ('Grayscale image', grayImage)
cv2.waitKey (0)

# hsv
hsvColorSpace = cv2.cvtColor (image, cv2.COLOR_BGR2HSV)
cv2.imshow ('HSV color space', hsvColorSpace)
cv2.waitKey (0)

# l*a*b
labColorSpace = cv2.cvtColor (image, cv2.COLOR_BGR2LAB)
cv2.imshow ('LAB', labColorSpace)
cv2.waitKey (0)