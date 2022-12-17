#=====================
#IMPORT MODULES
#=====================
from psychopy import core, event, gui, visual, monitors  #For psychopy experiment functions
import os                      #For handling paths
import random                  #For randomizing conditions
from datetime import datetime  #For getting the date
import pandas as pd            #For storing results

#=====================
#PATH SETTINGS
#=====================
directory = os.getcwd()
path = os.path.join(directory, 'dataFiles') #create path to save file in
if not os.path.exists(path):
   os.makedirs(path)
#=====================
#COLLECT PARTICIPANT INFO
#=====================
expInfo = {'subject_nr':0}
myDlg = gui.DlgFromDict(dictionary=expInfo) #Collect info in dialogue box
expInfo['date'] = datetime.now() 
filename = (str(expInfo['subject_nr']) + '_outputFile.csv')
date = datetime.now()
expInfo['date'] = f"{date.day}-{date.month}-{date.year}"
expFilename = (f"subject{expInfo['subject_nr']}_"
                       f"{expInfo['date']}_"
                       f"results.csv")
expFilename = os.path.join(path, expFilename)  # include directory

#=====================
#STIMULUS AND TRIAL SETTINGS
#=====================
nTrials = 10  # number of trials per block
nBlocks = 2  # number of blocks
stim_names = ['word1', 'word2', 'word3', 'word4']  # stimulus names
stim_extensions = ['.jpg', '.jpg', '.jpg', '.jpg']  # stimulus extensions for images
stim_size = 0.5  # stimulus size (in degrees of visual angle)
stim_ori = 0  # stimulus orientation (in degrees)
stim_loc = (0, 0)  # stimulus location (x, y coordinates in pixels)
stim_dur = 1  # stimulus duration 
start_message = 'Press any key to begin the experiment.'  # start message text

#=====================
#PREPARE CONDITION LISTS
#=====================
# Check if stimulus files exist
for i in range(len(stim_names)):
    if not os.path.exists(os.path.join(img_dir, stim_names[i] + stim_extensions[i])):
        print('Error: File not found:', os.path.join(img_dir, stim_names[i] + stim_extensions[i]))

# Create counterbalanced list of all conditions
conditions = []  # list to store conditions
for i in range(nTrials):
    conditions.append((stim_names[i % 4], stim_names[(i+1) % 4]))  # pair each stimulus with every other stimulus

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
# Define monitor settings
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1920, 1080])
win = visual.Window(
 fullscr=False, 
 monitor=mon, 
 size=(600,600), 
 color='grey', 
 units='pix'
)

# Define experiment start text
start_text = visual.TextStim(win, text=start_message, color=(1, 1, 1), pos=(0, 0), height=36)
# Define block start/end text
block_start_text = visual.TextStim(win, text='Press any key to begin block %d.', color=(1, 1, 1), pos=(0, 0), height=36)
block_end_text = visual.TextStim(win, text='End of block %d. Press any key to continue.', color=(1, 1, 1), pos=(0, 0), height=36)

# Define stimuli
stimuli = []
for i in range(len(stim_names)):
    stimuli.append(visual.ImageStim(win, image=os.path.join(img_dir, stim_names[i] + stim_extensions[i]), size=stim_size, ori=stim_ori, pos=stim_loc))

# Create response time clock
rt_clock = core.Clock()

#=====================
#START EXPERIMENT
#=====================
# Present start message text
start_text.draw()
win.flip()

# Wait for key press to begin experiment
event.waitKeys()

#=====================
#BLOCK SEQUENCE
#=====================
for iblock in range(nBlocks):
    # Present block start message
    block_start_text.setText(block_start_text.text % (iblock+1))
    block_start_text.draw()
    win.flip()
    
    event.waitKeys() # Wait for key press to begin block

    
    
    random.shuffle(conditions) # Randomize order of trials

    # Reset response time clock
    rt_clock.reset()

    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for itrial in range(nTrials):
        # Set stimuli and stimulus properties for the current trial
        stim1 = stimuli[stim_names.index(conditions[itrial][0])]
        stim2 = stimuli[stim_names.index(conditions[itrial][1])]

        # Empty keypresses
        event.clearEvents()

        #=====================
        #START TRIAL
        #=====================   
        # Draw stimulus 1
        stim1.draw()
        win.flip()

        # Wait time (stimulus duration)
        core.wait(stim_dur)

        # Draw stimulus 2
        stim2.draw()
        win.flip()

        # Wait for response
        keys = event.waitKeys()

        # Collect subject response for that trial
        response = keys[0]

        # Collect subject response time for that trial
        rt = rt_clock.getTime()

 

    # Present block end message
    block_end_text.setText(block_end_text.text % (iblock+1))
    block_end_text.draw()
    win.flip()

    # Wait for key press to end block
    event.waitKeys()


results.to_csv(experiment_filename, index=False) #-write data to a file
win.close()# Close window
