from ColorDetector import ColorDetector
from ImageProcessor import ImageProcessor

colorDetector = ColorDetector()
imageProcessor = ImageProcessor()

imageProcessor.readImageAndIdentifyColor("../dataset/B.jpg", colorDetector, showHSV=False)
#runcimageProcessor.readVideoAndIdentifyColor(colorDetector, showHSV=False)
