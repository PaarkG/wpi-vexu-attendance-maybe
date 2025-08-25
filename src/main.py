import cv2
import zxingcpp
import numpy as np
import requests
import json

WEBHOOK_URL = "https://discord.com/api/webhooks/1409354480423534592/T_AiUvXiW0Go7d4MQAV1tGZKHoYCFAJ0TusVWWtUTQSmd8sBm2CVwwhjgLa4TtjVg-tO"

database = {
    "901049842": {"name": "Kevin", "present": False}
}

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
        return name + " just left the workshop!"
    else:
        return name + " just entered the workshop!"

capture = cv2.VideoCapture(0)

while True:
    # ret, frame = capture.read()
    frame = cv2.imread("src/testcode3.jpeg")

    # cv2.imshow("dumbass image", frame)
    barcodes = check_image_for_barcodes(frame)

    for barcode in barcodes:
        if barcode.text in database:
            send_message_to_discord(get_message_from_id(barcode.text))

    cv2.waitKey(1)
