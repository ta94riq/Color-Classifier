import cv2
import numpy as np
from collections import OrderedDict
from scipy.spatial import distance as dist

class ColorDetector:
	def __init__(self):
		colors = OrderedDict(
			{
				"red"	: (255, 0, 0),
				"green"	: (0, 255, 0),
				"blue"	: (0, 0, 255)
			}
		)

		self.hsv = np.zeros((len(colors), 1, 3), dtype="uint8")
		self.colorNames = []
		
		for (i, (name, rgb)) in enumerate(colors.items()):
			self.hsv[i] = rgb
			self.colorNames.append(name)

		self.hsv = cv2.cvtColor(self.hsv, cv2.COLOR_RGB2HSV)

	def label(self, image):
		mean = cv2.mean(image)[:3]
		minDist = (np.inf, 0)

		for (i, row) in enumerate(self.hsv):
			d = dist.euclidean(row[0], mean)
			if d < minDist[0]:
				minDist = (d, i)
		
		return self.colorNames[minDist[1]]
