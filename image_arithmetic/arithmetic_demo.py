from __future__ import print_function
import numpy as np
import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to image')
args = vars (ap.parse_args())

# read the image
image = cv2.imread (args['image'])


print ()
print ()
# print the max of 255
print ('max of 255 {}'.format(cv2.add(np.uint8([200]), np.uint8([100]))))
print ('min of 0 {}'.format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

print ()
print ()	
