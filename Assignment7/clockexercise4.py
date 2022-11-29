from psychopy import visual, monitors, event, core
import os

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon)

main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

stims = ['face01.jpg', 'face02.jpg', 'face03.jpg']
nTrials=3
nBlocks=2
my_image = visual.ImageStim(win,units="pix",size=(400,400))
trial_timer = core.Clock() 
block_timer = core.Clock()
for block in range(nBlocks):
    block_timer.reset()
    for trial in range(nTrials):
        trial_timer.reset()
        my_image.draw()
        while trial_timer.getTime()<=2:
            print('Trial'+str(trial)+" " +str(trial_timer.getTime()))
            my_image.image = os.path.join(image_dir,stims[trial])
            my_image.draw() 
            win.flip() 
    print('Block'+str(block)+" " +str(block_timer.getTime()))
win.close()