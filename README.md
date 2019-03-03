# SwaipuWaifu
Deep learning model trained via Clarifai on data scraped from Yuki's Tinder for automated swiping

## Requirements

### Python packages

- Python versions 3.5.2
absl-py==0.2.2
applescript==0.0.1
astor==0.7.1
beautifulsoup4==4.6.3
cached-property==1.5.1
certifi==2018.10.15
chardet==3.0.4
clarifai==2.4.1
configparser==3.5.0
cycler==0.10.0
decorator==4.3.0
detect==0.0.2
future==0.17.1
gast==0.2.0
googleapis-common-protos==1.5.5
graphviz==0.8.4
grpcio==1.13.0
gspread==3.0.1
h5py==2.8.0
httplib2==0.11.3
idna==2.7
jsonschema==2.6.0
Keras==2.2.0
Keras-Applications==1.0.2
Keras-Preprocessing==1.0.1
kiwisolver==1.0.1
Markdown==2.6.11
matplotlib==2.2.2
numpy==1.14.5
oauth2client==4.1.3
only==1.0.3
opencv-python==3.4.3.18
pgrep==0.0.0
Pillow==5.3.0
playsound==1.2.2
protobuf==3.6.0
psutil==5.4.8
public==2.0.1
pyasn1==0.4.4
pyasn1-modules==0.2.2
PyAutoGUI==0.9.38
pydot==1.2.4
pygame==1.9.4
PyMsgBox==1.0.6
pynder==0.0.13
pyparsing==2.2.0
Pypubsub==4.0.0
PyScreeze==0.1.18
python-dateutil==2.7.3
pyttsx==1.1
pyttsx3==2.7
PyTweening==1.0.3
pytz==2018.5
pywin32==224
PyYAML==3.13
requests==2.20.0
robobrowser==0.5.3
rsa==4.0
runcmd==0.0.3
scikit-learn==0.19.2
scipy==1.1.0
six==1.11.0
temp==1.0.2
tensorboard==1.9.0
tensorflow==1.9.0
termcolor==1.1.0
urllib3==1.24
vlc==0.1.1
Werkzeug==0.14.1
wxPython==4.0.3


## Run

### Data

- Input images
  - 5000 Tinder profile images "faces_of_tinder_profile" dataset from Kaggle
- Annotation
  - The images were divided into two categories "right" and "left" based on Yuki's preferences.

### How to use

#### Before usage
- Login to Clarifai
$ https://clarifai.com/developer/account/login

#### Step 0
- Download Tinder profile images into a file.
- run FaceCropper.py in the folder to crop all the faces from the images.
  - all the images of cropped faces would be saved in the same file location 
- Annotate the cropped Tinder profile images to get data to start with
  - Separate the faces into two different folders, “right” and “left”
- Split the annotated data into training and testing data.
  - 80% training 20% testing was used
- Upload the training data on the Clarifai account
  - make sure to upload both groups of images “right” and “left” separately

#### Step 1
- Run Training.py 
  - make sure to type the api_key on line16
  - change the train test split if necessary

#### Step 2
- Login to PCver of Tinder
$ https://tinder.com/app/recs
- Proceed further to the screen used to swipe left and right
- Run SwipuWaifu.py
  - quickly change back to the browser so that the software can start swiping

## Alternatives for Data collection
### WARNING: The Tinder account might be temporarily disabled/BANed when running scraper.py, as the server might detect rapid uncertain access from this strip of code. Run with your own risk.
- scraper.py can be used to scrape data (Tinder profile images) directly from Tinder
- Authenticate with the facebook account by inputing the login details in authenticate.py


