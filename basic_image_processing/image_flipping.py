import numpy as np
import argparse
import cv2

# handle the command-line arguments
ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to image')
args = vars (ap.parse_args())

# read the image
image = cv2.imread (args['image'])

# function to flip the image hosrizontally
flipped = cv2.flip (image, 1)
cv2.imshow ('Flipped horizontally', flipped)
cv2.waitKey(0)

# function to flip the image vertically
flipped = cv2.flip (image, -1)
cv2.imshow ('Flipped the image vertically', flipped)
cv2.waitKey(0)
