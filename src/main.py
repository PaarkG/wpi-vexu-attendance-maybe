import cv2
import zxingcpp
import numpy as np

database = {}

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.filter2D(frame, -1, np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]))

    cv2.imshow("dumbass image", frame)
    barcodes = zxingcpp.read_barcodes(frame)

    for barcode in barcodes:
        if barcode.text in database:
            print(database[barcode.text])
        else:
            database[barcode.text] = str(input("What is your name?"))

    cv2.waitKey(1)
