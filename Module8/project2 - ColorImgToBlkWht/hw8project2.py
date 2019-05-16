#!   /usr/bin/python
#  Exercise No.   2
#  File Name:     hw8project2.py
#  Programmer: 	  Jon Weber
#  Date: 		  Oct. 22, 2017
#
#   Problem Statement: Write a program that converts
#		a color image into grayscale.
#
#
#	Overall Plan:
#	1. Introduce program and request image file name
# 2. Verify file is valid image
# 3. Draw image to screen
#	4. Detect image size and convert pixels within those parameters
# 5. Draw new grayscale pixels to screen
# 6. Save grayscale image as new file
#
#  import the necessary python libraries
from graphics import *

def grayScale(img):
	# Detect image width and height
	imgWidth = img.getWidth()
	imgHeight = img.getHeight()
	# For each row in the image from top to bottom:
	for row in range(1, imgHeight):
		# For each column in each row in the image from left to right
		for col in range(1, imgWidth):
			# Get pixel rgb value and save each value to variable
			r, g, b = img.getPixel(col, row)
			# Convert color value to grayscale
			brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
			# Update image with new grayscale pixel value
			img.setPixel(col, row, color_rgb(brightness, brightness, brightness))

def interface(file):
	# Create GUI window and set window coordinates
	win = GraphWin("Grayscale", 960, 720)
	win.setCoords(0, 0, 96, 72)
	# Print image to screen, centered
	img = Image(Point(48, 36), file).draw(win)
	
	# Await user mouse click
	print("Please click the image to begin applying filter")
	win.getMouse()
	# Alert user of time delay
	print("\nProcessing...")
	print("This may take a few seconds")
	# Convert image
	grayScale(img)
	# Await user response
	print("\nPlease click the new image to save and close")
	win.getMouse()

	# Save grayscale image file to disk
	fileName, ext = file.split(".")
	outputFile = fileName + "_grayscale"
	outfileName = outputFile + "." + ext
	img.save(outfileName)

def main():
	# Introduce the program
	print("\nThis program will apply a grayscale image")
	print("filter to a gif or ppm image type")
	print("\nLet's begin:")
	input("Press <ENTER> to continue\n")
	
	# Request image file from user to convert
	file = input("What is the name of the image file to grayscale? ")
	
	# Process GUI
	print("\nOpening...")
	try:
		interface(file)
	except:
		print("Please input a valid image with a .gif or .ppm file extension.")

main()
