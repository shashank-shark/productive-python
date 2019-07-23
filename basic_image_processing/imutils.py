import cv2
import numpy as np

#-------------------------------
# function for image translation
def translate_image (image, x, y):
	# feeding the translation matrix
	M = np.float32 ([[1,0,x],[0,1,y]])
	shifted = cv2.warpAffine (image, M, (image.shape[1], image.shape[0]))

	# note that we are returning the wrapAffined image with M
	return shifted

#--------------------------------
# function to rotate the image
def rotate_image (image, angle, center=None, scale=1.0):
	(h, w) = image.shape[:2]

	# if center is None we calculate the center
	if center is None:
		center = (w // 2, h // 2)

	M = cv2.getRotationMatrix2D (center, angle, scale)

	# calculate the rotated matrix
	rotated = cv2.warpAffine (image, M, (w,h))

	return rotated

#---------------------------------
# function to resize the image
def resize_image (image, width = None, height=None, inter=cv2.INTER_AREA):
	dim = None

	(h, w) = image.shape[:2]

	if width is None and height is None:
		# no resizing is required
		return image

	if width is None:
		# ratio is required height over original height of the image
		r = height / float(h)

		# calculate the new dimension
		dim = (int(w * r), height)
	else:
		r = width / float (w)
		dim = (width, int (h * r))

	resized = cv2.resize (image, dim, interpolation=inter)

	return resized