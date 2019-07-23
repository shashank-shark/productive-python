import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to image')
args = vars (ap.parse_args())

# read the image and conver to grayscale
image = cv2.imread (args['image'])
grayScaleImage = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur (grayScaleImage, (5,5), 0)
cv2.imshow ('Initial Gaussian Blurred grayscale image', blurred)

# apply thresholding
(T, thresh) = cv2.threshold (blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow ('Threshold Binary', thresh)

(T, threshInv) = cv2.threshold (blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow ('Threshold Binary Inverse', threshInv)
cv2.waitKey (0)