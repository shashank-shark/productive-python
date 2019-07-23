import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to image')
args = vars (ap.parse_args())

# read the image
image = cv2.imread (args['image'])

# convert the image to grayscale
grayScaleImage = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)

# apply the gaussian blur
blurred = cv2.GaussianBlur (image, (5,5), 0)
cv2.imshow ('Image after gaussian blur', image)

# apply the canny edge detection
canny = cv2.Canny (image, 30, 150)
cv2.imshow ('Canny Edge Detection', canny)
cv2.waitKey (0)