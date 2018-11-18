import authenticate as auth
import numpy as np
import pynder
import cv2
import urllib.request


def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
    return image

fb_id = "100014199346299"
token = auth.get_access_token()
session = pynder.Session(facebook_id = fb_id, facebook_token = token)

data = open("data.txt", "a+")

while True:
    users = session.nearby_users()
    for user in users:
        photos = user.get_photos()
        print("Fetched user photos..")
        for photo in photos:
            img = url_to_image(photo)
            cv2.imshow("picture", img)
            cv2.waitKey(2000)

            input_string = "Write 1 to like. Write 0 to dislike."
            ans = str(input(input_string)).lower()

            data.write(photo + "," +str(ans))