import cv2
import argparse
import numpy as np

# handle the args
ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to the image')
args = vars (ap.parse_args())

# read the image
image = cv2.imread (args['image'])
cv2.imshow ('Original Image', image)
cv2.waitKey(0)

# generate the mask matrix
mask = np.zeros (image.shape[:2], dtype='uint8')
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)

# draw the rectangle
cv2.rectangle (mask, (cX - 75, cY - 75), (cX + 75, cY + 75), 255, -1)
cv2.imshow ('Rectangle that is drawn', mask)

# we do the bitwise_and to get rid of other regions
masked = cv2.bitwise_and (image, image, mask=mask)
cv2.imshow ('This is the masked image', masked)
cv2.waitKey (0)