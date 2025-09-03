import cv2
import zxingcpp
import numpy as np
import requests
import json
import time

WEBHOOK_URL = "https://discord.com/api/webhooks/1409354480423534592/T_AiUvXiW0Go7d4MQAV1tGZKHoYCFAJ0TusVWWtUTQSmd8sBm2CVwwhjgLa4TtjVg-tO"

database = ""

with open("src/members.json") as file:
    database = json.load(file)

def send_message_to_discord(message_text):
    data = {
        "id": "1409354480423534592",
        "type": 1,
        "content": message_text
    }

    data_json = json.dumps(data)
    requests.post(WEBHOOK_URL, data)

def check_image_for_barcodes(image):
    return zxingcpp.read_barcodes(image)

def get_message_from_id(id):
    person_info = database[id]
    name = person_info["name"]
    present = person_info["present"]
    person_info["present"] = not present
   
    if present:
        time_present = time.time() - person_info["time_signed_in"]
        person_info["time_signed_in"] = -1
        return name + " just left the workshop! They were present for " + str(int(time_present)) + " seconds."
    else:
        person_info["time_signed_in"] = time.time()
        return name + " just entered the workshop!"

capture = cv2.VideoCapture(0)
kernel = np.array([[-1, 1, -1], [-1, 5, -1], [-1, 1, -1]])

while True:
    ret, frame = capture.read()
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.filter2D(frame, -1, kernel)
    # frame = cv2.imread("src/testcode1.jpeg")
    cv2.imshow("image?", frame)

    # cv2.imshow("dumbass image", frame)
    barcodes = check_image_for_barcodes(frame)

    for barcode in barcodes:
        print('barcode found')
        print(barcode.text)
        if str(barcode.text) in database:
            send_message_to_discord(get_message_from_id(barcode.text))

    cv2.waitKey(1)