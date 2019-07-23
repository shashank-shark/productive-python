import cv2
import argparse
import numpy as np
import mahotas

ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to image')
args = vars (ap.parse_args())

# read the image
image = cv2.imread (args['image'])
image = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur (image, (5,5), 0)
cv2.imshow ('Image', image)

T = mahotas.thresholding.otsu (blurred)
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not (thresh)
cv2.imshow ('Otsu', thresh)
cv2.waitKey (0)

