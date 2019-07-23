import numpy as np
import cv2

# create out own manual image
canvas = np.zeros ((300,300,3), dtype="uint8")

# print the channels of the image
cv2.imshow ('Canvas image', canvas)

# now draw a green rectangle here
green = (0, 255, 0)

cv2.line (canvas, (0, 0), (300, 300), green)
cv2.imshow ('Canvas image with green border', canvas)
cv2.waitKey(0)