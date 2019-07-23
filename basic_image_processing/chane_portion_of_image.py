from __future__ import print_function
import argparse
import cv2

# first get the arg-parser ready
ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help="path to the image")
args = vars (ap.parse_args())

# print the value stored in the dict
print ('The path to the image is : ', args)

# now read the image
image = cv2.imread (args['image'])
cv2.imshow ('Image that is read now', image)
cv2.waitKey(0)

# select a portion of the image and decrease the intensity
corner = image[0:100, 0:100]
cv2.imshow ('Corner part of the image', corner)
cv2.waitKey(0)

# now change the intensity of the corner
image[0:100, 0:100] = (0, 255, 0)
cv2.imshow ('Image after modification', image)
cv2.waitKey(0)