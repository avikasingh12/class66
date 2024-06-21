# Importing Library
import numpy as np
import cv2


inputPath = 'static/lion.png'


originalImage = cv2.imread(inputPath)


# ------------Convert image to Grayscale --------------


grayscaleImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)


outputPath = 'converted/grayScale.png'
cv2.imwrite(outputPath, grayscaleImage)

cv2.imshow('Grayscale Image', grayscaleImage)
cv2.waitKey(0)


print('Converted Grayscale image saved to disk : ' + outputPath)


# ----------------- Convert image to Oil Painting -----------------------

oilImg = cv2.xphoto.oilPainting(originalImage, size=7, dynRatio=1)
outputPath = 'converted/oilpainting.png'
# Save the oil painting effect image to disk
cv2.imwrite(outputPath, oilImg)

cv2.imshow('Oil Paint Image', oilImg)
cv2.waitKey(0)

# Display a message indicating that the image has been saved



# ----------------- Convert image to Sketch Image ---------------

# Invert the grayscale image
invertedImg = 255 - grayscaleImage

# Apply Gaussian blur
blurredImg = cv2.GaussianBlur(invertedImg,(21,21),0)

# Blend the grayscale image and the blurred image using the color dodge blend mode
sketchImg= cv2.divide(grayscaleImage,255-blurredImg,scale = 256)

# Save the sketch image to disk
outputPath='converted/sketchImage.png'

# Display the converted image
cv2.imwrite(outputPath,sketchImg)

# Display a message indicating that the image has been saved
