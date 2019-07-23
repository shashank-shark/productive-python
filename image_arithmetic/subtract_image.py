import argparse
import cv2
import numpy as np

# handle the args
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="input the image path")
args = vars (ap.parse_args())

# read the image
image = cv2.imread (args['image'])

# we apply the cv2.subtract function to make the image darker
M = np.ones (image.shape, dtype='uint8') * 50

subtracted = cv2.subtract (image, M)
cv2.imshow ('Subtracted image', subtracted)
cv2.waitKey (0)

cv2.imshow ('Original Image', image)
cv2.waitKey (0)