from matplotlib import pyplot as plt
import cv2
import argparse
import numpy as np

# handle the args
ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to the image')
args = vars (ap.parse_args())

# read the image
image = cv2.imread(args['image'])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# now apply the equization
equ = cv2.equalizeHist (image)

cv2.imshow ('Histogram Equization', np.hstack([image, equ]))
cv2.waitKey(0)