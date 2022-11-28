from psychopy import visual, monitors, event, core
import os
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) 
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')
fix_text = visual.TextStim(win, text='+')
start_msg = "Welcome to the experiment!"
block_msg = "Please wait until the next image appears!"
end_msg = "This is the end of the trial."
stims = ['face01.jpg', 'face02.jpg', 'face03.jpg']
my_image = visual.ImageStim(win)
nTrials = 3
start_text = visual.TextStim(win, text=start_msg)
start_text.draw()
win.flip()
core.wait(2)
wait_timer = core.Clock()
wait_timer.getTime()
for trial in range(nTrials):
    my_image.image = os.path.join(image_dir,stims[trial])
    #=====================
    #START TRIAL
    #=================== 
    block_text = visual.TextStim(win, text=block_msg)
    block_text.draw()
    #-draw fixation
    fix_text.draw()
    #-flip window
    win.flip()
    #-wait time (stimulus duration)
    core.wait(0.5)

    #-draw image
    my_image.draw()
    #-flip window
    win.flip()
    imgStartTime = wait_timer.getTime()
    #-wait time (stimulus duration)
    core.wait(2)
    imgEndTime = wait_timer.getTime()

    #-draw end trial text
    end_text = visual.TextStim(win, text=end_msg)
    end_text.draw()
    #-flip window
    win.flip()
    #-wait time (stimulus duration)
    core.wait(2)
    
    print(imgEndTime - imgStartTime)

win.close()