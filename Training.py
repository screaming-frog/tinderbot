from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from glob import glob
import random

def scrambled(orig): ##shuffling a list of image locations
    dest = orig[:]
    random.shuffle(dest)
    return dest

def batch(iterable, n=128):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

app = ClarifaiApp(api_key='72274b24aa40462ab3d685c8a7a89c97')

img_locs = scrambled(glob(".//persons_cropped//*.jpg")) #all photos in the 'no' set, shuffled
no_train = img_locs[:401] #select the training data for 'no'

yes_train = glob(".//yes//*.jpg")[:401] #same for 'yes'

no_val = img_locs[401:]
yes_val = img_locs[401:]

yes_img_list = [ClImage(filename = image, concepts=["yes"]) for image in yes_train ] #creating lists of Clarifai data points and labels
no_img_list = [ClImage(filename = image, concepts=["no"]) for image in no_train ]
test_nos = [ClImage(filename = image) for image in no_val ]
test_yes = [ClImage(filename = image) for image in yes_val ]

yes_img_list = batch(yes_img_list) #max batch size is 128 for upload
no_img_list = batch(no_img_list)
test_nos = batch(test_nos)
test_yes = batch(test_yes)

for img_batch in yes_img_list:
    app.inputs.bulk_create_images(img_batch) #uploading lists
for img_batch in no_img_list:
    app.inputs.bulk_create_images(img_batch)

model = app.models.create(model_id="swaipuwaifu", concepts=["yes", "no"],concepts_mutually_exclusive=True, closed_environment=True) #create model
model = model.train() #training model

yes_img_list = list(yes_img_list) #turn all image generator objects back to lists
no_img_list = list(no_img_list)
test_nos = list(test_nos)
test_yes = list(test_yes)

######################### TESTING ############################
model = app.models.get('swaipuwaifu')
preds = model.predict(test_nos[0])
yes_preds = model.predict(test_yes[0])