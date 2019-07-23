import cv2
import argparse
import numpy as np

# handle args
ap = argparse.ArgumentParser()
ap.add_argument ('-i', '--image', required=True, help='path to image')
args = vars (ap.parse_args())

# read the image
image = cv2.imread (args['image'])

rectangle = np.zeros ((300,300), dtype='uint8')
cv2.rectangle (rectangle, (25,25), (255, 255), 255, -1)
cv2.imshow ('Initial Rectangle', rectangle)
cv2.waitKey (0)

circle = np.zeros ((300,300), dtype='uint8')
cv2.circle (circle, (150, 150), 150, 255, -1)
cv2.imshow ('Initial circle', circle)
cv2.waitKey (0)

# now we perform bitwise_and
bitwiseAndOperation = cv2.bitwise_and (rectangle, circle)
cv2.imshow ('Bitwise AND', bitwiseAndOperation)
cv2.waitKey (0)

# now we perform bitwise _or
bitwiseOrOperation = cv2.bitwise_or (rectangle, circle)
cv2.imshow ('Bitwise OR', bitwiseOrOperation)
cv2.waitKey (0)

# now we perform bitwise_xor
bitwiseXorOperation = cv2.bitwise_xor (rectangle, circle)
cv2.imshow ('Bitwise XOR', bitwiseXorOperation)
cv2.waitKey (0)

# now we perform bitwise_not
bitwiseNotOperation = cv2.bitwise_not (rectangle, circle)
cv2.imshow ('Bitwise NOT', bitwiseNotOperation)
cv2.waitKey (0)