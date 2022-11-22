from psychopy import visual, monitors, event
import os
import numpy as np

mon = monitors.Monitor('myMonitor', width = 13.5, distance = 60)
mon.setSizePix([3000,2000])
win = visual.Window(monitor=mon, size=(800,800), color=(-1,-1,-1))
my_image = visual.ImageStim(win, units='pix', size = (400,400))

os.chdir('/Applications')
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

stims = ['face01.jpg','face02.jpg','face03.jpg']
nTrials=3 
my_image = visual.ImageStim(win,units="pix",size=(400,400))


for trial in range(nTrials): 
    my_image.image = os.path.join(image_dir,stims[trial])
    my_image.draw() 
    win.flip()
    event.waitKeys()
    
win.close()