import numpy as np
import cv2
import pandas as pd
def getImage():
    image = cv2.VideoCapture(0)

    while(True):
        rect, img = image.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #change the colour to grayscale
        img = cv2.resize(img, (200, 200)) #defines the dimension as 200*200
        cv2.imshow('img1', img)  # display the captured image

        if cv2.waitKey(1) & 0xFF == ord('y'):  # save on pressing 'y'

            cv2.imwrite('Image.png', img) #saves to the folder as image.png
            cv2.destroyAllWindows()
            break

    image.release()

getImage()
