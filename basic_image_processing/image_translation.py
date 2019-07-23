import numpy as np
import argparse
import imutils
import cv2

ap =argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to the image')
args = vars (ap.parse_args())

image = cv2.imread (args["image"])
cv2.imshow ('Original Image', image)

# code for translation matrix is written in imutils file

# call the function to rotate the image
shifted = imutils.translate_image (image, 0, 100)
cv2.imshow ('Shifted image is : ', shifted)
cv2.waitKey(0)