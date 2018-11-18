from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import cv2

from glob import glob


app = ClarifaiApp(api_key='15721892aa2e4add86a49586c29871f5')
model = app.models.get('face-v1.3')


def face_cropper_coords(image_name):
    # image_name = cwd+'/'+image_name
    img = cv2.imread(image_name)
    height, width, channels = img.shape
    image = ClImage(filename=image_name)
    prediction = model.predict([image])
    crop_coord_list = []

    for region in prediction["outputs"][0]["data"]["regions"]:
        boxcoord = region["region_info"]["bounding_box"]
        bottom_row = int(round(height * (boxcoord["bottom_row"])))
        top_row = int(round(height * (boxcoord["top_row"])))
        left_col = int(round(width * boxcoord["left_col"]))
        right_col = int(round(width * boxcoord["right_col"]))
        crop_coord_list.append([bottom_row, top_row, left_col, right_col])

    return crop_coord_list


def face_cropper_img(image_name):

    img = cv2.imread(image_name)
    height, width, channels = img.shape
    image = ClImage(filename=image_name)
    prediction = model.predict([image])
    regions = prediction["outputs"][0]["data"]
    if len(regions) == 0:
        return# cv2.imread('black.png')

    for region in prediction["outputs"][0]["data"]["regions"]:
        boxcoord = region["region_info"]["bounding_box"]
        bottom_row = int(round(height * (boxcoord["bottom_row"])))
        top_row = int(round(height * (boxcoord["top_row"])))
        left_col = int(round(width * boxcoord["left_col"]))
        right_col = int(round(width * boxcoord["right_col"]))
        crop_img = img[top_row:bottom_row, left_col:right_col]

        #         print(bottom_row,top_row, left_col,right_col)

    return crop_img

img_locs = glob("*.jpg") # return list of all jpgs in current directory

for img_loc in img_locs[:100]: #crop first 100 faces in img_locs
    img = face_cropper_img(img_loc)
    cv2.imwrite('persons_cropped/'+img_loc, img) #save to subfolder