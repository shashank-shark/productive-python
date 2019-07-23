from matplotlib import pyplot as plt
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

# now split the channels as we are dealing with colors
channels = cv2.split (image)
colors = ('b', 'g', 'r')
plt.figure ()

plt.title ('Flattened Color Histogram')
plt.xlabel ('Bins')
plt.ylabel ('# of Pixels')

for (chan, color) in zip (channels, colors):
	hist = cv2.calcHist ([chan], [0], None, [256], [0,256])
	plt.plot (hist, color=color)
	plt.xlim ([0,256])

fig = plt.figure ()

ax = fig.add_subplot (131)
hist = cv2.calcHist ([channels[1], channels[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow (hist, interpolation='nearest')
ax.set_title ('2D color histogram for G and B')
plt.colorbar(p)


ax = fig.add_subplot (132)
hist = cv2.calcHist ([channels[1], channels[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow (hist, interpolation='nearest')
ax.set_title ('2D color histogram for G and R colors')
plt.colorbar(p)


ax = fig.add_subplot (133)
hist = cv2.calcHist ([channels[0], channels[1]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow (hist, interpolation='nearest')
ax.set_title ('2D color histogram for B and R')
plt.colorbar(p)

hist = cv2.calcHist ([image], [0, 1, 2], None, [8, 8, 8, ], [0, 256, 0, 256, 0, 256])
plt.show()