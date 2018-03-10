import cv2

class ImageProcessor:
	def readImage(self, path):
		return cv2.imread(path)
		
	def showImage(self, title, image):
		cv2.imshow(title, image)

	def convertToHSV(self, image):
		return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	def splitHSVComponents(self, image):
		h,s,v = cv2.split(self.convertToHSV(image))
		return h, s, v

	def showHSVComponents(self, image):
		h, s, v = self.splitHSVComponents(image)

		hh = h.copy()
		ss = s.copy()
		vv = v.copy()
		hh.fill(255)
		ss.fill(255)
		vv.fill(255)

		hImage = cv2.cvtColor(cv2.merge([h, ss, vv]), cv2.COLOR_HSV2BGR)
		sImage = cv2.cvtColor(cv2.merge([hh, s, vv]), cv2.COLOR_HSV2BGR)
		vImage = cv2.cvtColor(cv2.merge([hh, ss, v]), cv2.COLOR_HSV2BGR)

		self.showImage("H", hImage)
		self.showImage("S", sImage)
		self.showImage("V", vImage)
			
	def readImageAndIdentifyColor(self, path, colorDetector, showHSV):
		image = self.readImage(path)

		colorName = colorDetector.label(self.convertToHSV(image))
		cv2.putText(image, colorName, (10, 50), cv2.FONT_ITALIC, 2, 255)
		self.showImage("image", image)

		if showHSV == True:
			self.showHSVComponents(image)

		cv2.waitKey()


	def readVideoAndIdentifyColor(self, colorDetector, showHSV):
		cap = cv2.VideoCapture(0)

		while (True):
			ret, image = cap.read()
			
			colorName = colorDetector.label(self.convertToHSV(image))
			cv2.putText(image, colorName, (10, 50), cv2.FONT_ITALIC, 2, 255)
			self.showImage("image", image)

			if showHSV == True:
				self.showHSVComponents(image)

			key = cv2.waitKey(1)
			if key == 1048689:
				break

		cap.release()
		cv2.destroyAllWindows()
