import pyautogui as pag
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import cv2
import time
import pyttsx3
import random


engine = pyttsx3.init() # initialise text to speech
positive_speech = ['Yes please', 'Hell yeah','Why not?', 'Sure', 'Yes'] #Possible voice lines
negative_speech = ['I respectfully decline', 'No comment','Next!', 'Nah', 'Its not you, its me', 'sai yo naara']

app = ClarifaiApp(api_key='72274b24aa40462ab3d685c8a7a89c97') #init the ml stuff
crop_model = app.models.get('face-v1.3')
model = app.models.get('swaipuwaifu')


def face_cropper_img(image_name):

    img= cv2.imread(image_name)
    height, width, channels = img.shape
    image = ClImage(filename= image_name)
    prediction = crop_model.predict([image])
    regions = prediction["outputs"][0]["data"]

    if len(regions) == 0:
        return

    for region in prediction["outputs"][0]["data"]["regions"]:
        boxcoord = region["region_info"]["bounding_box"]
        bottom_row = int(round(height*(boxcoord["bottom_row"])))
        top_row = int(round(height*(boxcoord["top_row"])))
        left_col = int(round(width*boxcoord["left_col"]))
        right_col = int(round(width*boxcoord["right_col"]))
        crop_img = img[top_row:bottom_row, left_col:right_col]

        #         print(bottom_row,top_row, left_col,right_col)
    cv2.imwrite(image_name+'cropped.jpg', crop_img)
    return ClImage(filename=image_name+'cropped.jpg')


width, height = pag.size()
desperation = float(input('Enter desperation factor: '))
while True:
    time.sleep(2)

    for i in range(9):
        pag.press('space')
        time.sleep(0.2)
        screencap = pag.screenshot(str(i) + '.jpg', region=(width / 2, height / 10, width / 4, height * 2 / 3))

    cropped = [face_cropper_img(str(j)+'.jpg') for j in range(3)]
    cropped = [x for x in cropped if x is not None]
    print(cropped)
    if cropped == []:
        pag.press('left')
        continue
    preds = model.predict(cropped)

    sentiment = 0
    for pred in preds['outputs']:
        res0 = pred['data']['concepts'][0]
        res1 = pred['data']['concepts'][1]

        if res0['id'] == 'no':
            sentiment += res1['value']-res0['value']/desperation

        else:
            sentiment += res0['value'] - res1['value']/desperation
    print(sentiment)


    if sentiment > 0:
        engine.say(random.sample(positive_speech,1)[0])
        engine.runAndWait()
        pag.press('right')
    else:
        engine.say(random.sample(negative_speech,1)[0])
        engine.runAndWait()
        pag.press('left')
