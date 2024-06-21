Process and Save Images
=========================


In this activity, you will learn to process an image and save  the output image on your computer.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10475812/sketch.png" width = "480" height = "320">


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10475883/converted.png" width = "480" height = "320">

Follow the given steps to complete this activity:
1. ### Convert Image to sketch Image
* Open the file main.py.
* Declare a variable `invertedImg` .
* Subtract the `grayscaleImage` from 255 and set it as the value for `invertedImg` variable.


    `invertedImg = 255 - grayscaleImage`


* Apply the gaussian blur to the `imvertedImg`.


    `blurredImg = cv2.GaussianBlur(invertedImg, (21, 21), 0)`


* Blend the grayscale image and the blurred image using the color dodge blend mode.


    `sketchImg = cv2.divide(grayscaleImage, 255 - blurredImg, scale=256)`


* Display the converted image.


    `cv2.imshow('Sketch Image', sketchImg)`


* Assign the `esc` key to close the opened image.
    `cv2.waitKey(0)`


2. ### Save the processed Image


* Create the `outputPath` variable and store the path for the image to be saved.


    `outputPath = 'converted/sketch.png')`


* Use the `cv2.imwrite()` function, pass `outputpath`, and `sketchImg` as parameters to save the image.


    `cv2.imwrite(outputPath, sketchImg)`


* Display a message on the terminal indicating that the image has been saved.


    `print('Converted Sketch image saved to disk: ' + outputPath)`


* Save the oil painting effect image to disk.


    `outputPath = 'converted/oilPainting.png`


    `cv2.imwrite(outputPath, oilImg)`


* Display a message indicating that the Oil Paint image has been saved.


    `print('Converted Oil Paint image saved to disk: ' + outputPath)`


* Save the grayscaleimage to disk.


    `outputPath = 'converted/grayScale.png`


    `cv2.imwrite(outputPath, grayscaleImage)`


* Display a message indicating that the grayscale image has been saved.


    `print('Converted Grayscale image saved to disk : ' + outputPath)`


* Save and run the code to check the output.
