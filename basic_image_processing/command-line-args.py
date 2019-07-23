# import the necessary packages
from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument ("-i", "--image", required=True, help="Path to the image")
args = vars (ap.parse_args())

# now args contains the path of the image inside the dictionary
print (args)

# Now read the image from the disk
image = cv2.imread (args['image'])

print ("The height of the image is {} pixels".format(image.shape[0]))
print ("The width of the image is {} pixels".format(image.shape[1]))
print ("The channels in the image is {} pixels".format(image.shape[2]))

cv2.imshow ("Image", image)
cv2.waitKey(0)

# save the image to the disk
cv2.imwrite ('before_image.jpg', image)

# now we write the code for some pixel manipulation
(b,g,r) = image[0,0]
print ("The pixel at the postion (0,0) is of the value : RED : {}, GREEN:{}, BLUE:{} ".format(r,g,b))