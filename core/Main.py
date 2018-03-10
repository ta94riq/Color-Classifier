import argparse
from ColorDetector import ColorDetector
from ImageProcessor import ImageProcessor


argumentParser = argparse.ArgumentParser()
argumentParser.add_argument("-s", "--source", required=True, help="Sourse to read.")
argumentParser.add_argument("-i", "--image", required=False, default="dataset/B.jpg", help="Path to image.")
arguments = vars(argumentParser.parse_args())

colorDetector = ColorDetector()
imageProcessor = ImageProcessor()

if arguments["source"] == "camera":
    imageProcessor.readVideoAndIdentifyColor(colorDetector, showHSV=False)
else:
    imageProcessor.readImageAndIdentifyColor(arguments["image"], colorDetector, showHSV=False)