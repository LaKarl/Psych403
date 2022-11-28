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
countdown_timer = core.CountdownTimer()

for trial in range(nTrials):
    my_image.image = os.path.join(image_dir,stims[trial])
    countdown_timer.reset()
    countdown_timer.addTime(2)
    my_image.draw()
    while countdown_timer.getTime() >0:
        print('Trial'+str(trial)+' time =', countdown_timer.getTime())
        my_image.draw() 
        win.flip()

win.close()