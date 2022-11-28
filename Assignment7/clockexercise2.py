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
start_text = visual.TextStim(win, text=start_msg)

wait_timer = core.Clock()
wait_timer.getTime()
#Start Trial
wait_timer.reset()
last_time = 0
while wait_timer.getTime() <= 2: 
    fix_text.draw()
    my_image.draw()
    win.flip()
current_time = wait_timer.getTime()
print(current_time - last_time)
last_time = current_time
while 2 < wait_timer.getTime() <= 4: 
    fix_text.draw()
    my_image.draw()
    win.flip()
current_time = wait_timer.getTime()
print(current_time - last_time)
last_time = current_time

while 4 < wait_timer.getTime() <= 6: 
    fix_text.draw()
    my_image.draw()
    win.flip()
current_time = wait_timer.getTime()
print(current_time - last_time)
last_time = current_time