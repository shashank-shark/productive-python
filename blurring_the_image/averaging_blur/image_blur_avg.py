from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

# setup the argparse
ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to image')
args = vars (ap.parse_args())

# read the image
image = cv2.imread (args['image'])
cv2.imshow ('Original Image', image)

# averaging
blurred = np.hstack ([
	cv2.blur (image, (3, 3)),
	cv2.blur (image, (5, 5)),
	cv2.blur (image, (7, 7))])
cv2.imshow ('Averaged', blurred)
cv2.waitKey(0)

# using gaussian blur
blurred = np.hstack ([
	cv2.GaussianBlur (image, (3,3), 0),
	cv2.GaussianBlur (image, (5,5), 0),
	cv2.GaussianBlur (image, (7,7), 0)])
cv2.imshow ('Gaussian Blurring', blurred)
cv2.waitKey(0)

# median blur
blurred = np.hstack ([
	cv2.medianBlur (image, 3),
	cv2.medianBlur (image, 5),
	cv2.medianBlur (image, 7)])
cv2.imshow ('Median Blurring', blurred)
cv2.waitKey(0)

# bilateral filter
blurred = np.hstack ([
	cv2.bilateralFilter(image, 5, 21, 21),
	cv2.bilateralFilter (image, 7, 31, 31),
	cv2.bilateralFilter (image, 9, 41, 41)])
cv2.imshow ('Bilaterral Filter Blurring', blurred)
cv2.waitKey (0)