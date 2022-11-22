from psychopy import visual, monitors, event
import numpy as np

#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
mon = monitors.Monitor('myMonitor', width = 13.5, distance = 60)
mon.setSizePix([3000,2000])
win = visual.Window(monitor=mon, size=(800,800), color=(-1,-1,-1))
#-define experiment start text unsing psychopy functions
start_msg = "Welcome to the experiment!"
#-define block (start)/end text using psychopy functions
block_msg = "Press any key to continue."
end_trial_msg = "End of the trial"
#-define stimuli using psychopy functions (images, fixation cross)
stims = ['face01.jpg','face02.jpg','face03.jpg']
fix = visual.TextStim(win,text='+')
#=====================
#START EXPERIMENT
#=====================
#-present start message text
start_msg = "Welcome to the experiment!"
my_text = visual.TextStim(win, text=start_msg)

#-allow participant to begin experiment with button press
my_text = visual.TextStim(win, text=block_msg)
event.waitKeys()
#=====================
#BLOCK SEQUENCE
#=====================
#-for loop for nBlocks
for block in range(nBlocks):
    #-present block start message
    visual.TextStim(win, text=block_msg)
    #-randomize order of trials here
    np.random.shuffle(trials)
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    #-for loop for nTrials
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        my_image = visual.ImageStim(win,units="pix",size=(400,400))

        #=====================
        #START TRIAL
        #=====================  
        #-draw fixation
        fix_text.draw()
        #-flip window
        win.flip()

        #-wait time (stimulus duration)
        core.wait(3)
        
        #-draw image
        pic_loc = os.path.join(image_dir,'face01.jpg')
        my_image = visual.ImageStim(win, image=pic_loc)
        my_image.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(3)
        
        #-draw end trial text
        end_trial_text.draw()
        #-flip window
        win.flip()
        #-wait time (stimulus duration)
        core.wait(3)
#======================
# END OF EXPERIMENT
#======================        
#-close window
win.close()