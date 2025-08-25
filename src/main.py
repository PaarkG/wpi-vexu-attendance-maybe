import cv2
import zxingcpp
import numpy as np
import requests
import json

webhook_url = "https://discord.com/api/webhooks/1409354480423534592/T_AiUvXiW0Go7d4MQAV1tGZKHoYCFAJ0TusVWWtUTQSmd8sBm2CVwwhjgLa4TtjVg-tO"
database = {
    "901049842": "Kevin"
}

image = cv2.imread("src/testcode3.jpeg")
id = zxingcpp.read_barcodes(image)[0].text
text = "unknown user scanned"

if id in database:
    text = database[id] + " just signed in"

data = {
    "id": "1409354480423534592",
    "type": 1,
    "content": text
}

data_json = json.dumps(data)

requests.post(webhook_url, data)

# capture = cv2.VideoCapture(0)

# while True:
#     ret, frame = capture.read()
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     frame = cv2.filter2D(frame, -1, np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]))

#     cv2.imshow("dumbass image", frame)
#     barcodes = zxingcpp.read_barcodes(frame)

#     for barcode in barcodes:
#         if barcode.text in database:
#             print(database[barcode.text])
#         else:
#             database[barcode.text] = str(input("What is your name?"))

#     cv2.waitKey(1)
