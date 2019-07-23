from matplotlib import pyplot as plt
import cv2
import argparse
import numpy as np

# handle the args
ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to the image')
args = vars (ap.parse_args())

# read and convert image to GRAYSCALE
image = cv2.imread (args['image'])
grayImage = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
cv2.imshow ('Grayscale Image', grayImage)

# now we calculate the histogram
hist = cv2.calcHist ([image], [0], None, [256], [0,256])
plt.figure ()
plt.title ('Grayscale Histogram')
plt.xlabel ('Bins')
plt.ylabel ('# of Pixels')
plt.plot (hist)
plt.xlim ([0,256])
plt.show ()
cv2.waitKey (0)