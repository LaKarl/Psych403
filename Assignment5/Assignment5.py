#=====================
#IMPORT MODULES
#=====================
#-import numpy and/or numpy functions *
import numpy as np
#-import psychopy functions
from psychopy import core, gui, visual, event
#-import file save functions
import json
#-(import other functions as necessary: os...)
import os

#=====================
#PATH SETTINGS
#=====================
#-define the main directory where you will keep all of your experiment files
print(os.getcwd())

main_dir = os.getcwd()
#-define the directory where you will save your data
data_dir = os.path.join(main_dir,'data')
#-if you will be presenting images, define the image directory
image_dir = os.path.join(main_dir,'images')
#-check that these directories exist
print(image_dir)
print(data_dir)
os.path.isdir(image_dir)
if not os.path.isdir(image_dir):
    raise Exception("Could not find the path!")

#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
#get date and time
#-create a unique filename for the data

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
#-number of trials and blocks *
nTrials = 10
nBlocks = 2
#-stimulus names (and stimulus extensions, if images) *
cats = ['faces'] * 10
imgs = ['im1.png', 'im2.png', 'im3.png', 'im4.png', 'im5.png', 'im6.png', 'im7.png', 'im8.png', 'im9.png', 'im10.png']
#-stimulus properties like size, orientation, location, duration *
stimSize = [200,200];
stimDur = 1;
stimOrien = [10];
#-start message text *
sMessage = "Welcome to the experiment, press any key to begin!"

#=====================
#PREPARE CONDITION LISTS
#=====================
#-check if files to be used during the experiment (e.g., images) exist
pics = []
number = 0
while number < 10:
    number = number + 1
    if number < 10:
        pics.append('face' + str(number) + '.jpg')
    elif number == 10:
        pics.append('face' + str(number) + '.jpg')
        
ims_in_dir = sorted(os.listdir(image_dir))
for pic in pics:
    if pics == ims_in_dir:
        print(str(pic) + ' was found!')
        
if not pics == ims_in_dir:
    raise Exception("The image does not exist!")
#-create counterbalanced list of all conditions *
catimgs = list(zip(cats, imgs))
print(catimgs)

#=====================
#PREPARE DATA COLLECTION LISTS
#=====================
#-create an empty list for correct responses (e.g., "on this trial, a response of X is correct") *
cResp = []
cResp = np.zeros(20)
#-create an empty list for participant responses (e.g., "on this trial, response was a X") *
pResp = []
pResp = np.zeros(20)
#-create an empty list for response accuracy collection (e.g., "was participant correct?") *
accResp = []
accResp = np.zeros(20)
#-create an empty list for response time collection *
tResp = []
tResp = np.zeros(20)
#-create an empty list for recording the order of stimulus identities *
stimID = []
stimID = np.zeros(20)
#-create an empty list for recording the order of stimulus properties *
stimProp = []
stimProp = np.zeros(20)

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
#-define the window (size, color, units, fullscreen mode) using psychopy functions
#-define experiment start text unsing psychopy functions
#-define block (start)/end text using psychopy functions
#-define stimuli using psychopy functions
#-create response time clock
#-make mouse pointer invisible

#=====================
#START EXPERIMENT
#=====================
#-present start message text
#-allow participant to begin experiment with button press

#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks *
for thisBlock in range(nBlocks):
    print('Welcome to block: ' + str(thisBlock + 1))
    #-present block start message
    #-randomize order of trials here *
    np.random.shuffle(catimgs)
    
    #-reset response time clock here
    
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials *
    for thisTrial in range(nTrials):
       print('trial: ' + str(thisTrial + 1))
        #-set stimuli and stimulus properties for the current trial
        #-empty keypresses
        
        #=====================
        #START TRIAL
        #=====================   
        #-draw stimulus
        #-flip window
        #-wait time (stimulus duration)
        #-draw stimulus
        #-...
        
        #-collect subject response for that trial
        #-collect subject response time for that trial
        #-collect accuracy for that trial
        
#======================
# END OF EXPERIMENT
#======================        
#-write data to a file
#-close window
#-quit experiment