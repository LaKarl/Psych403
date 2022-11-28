from psychopy import visual, monitors, event, core
import os
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon) 

main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

refresh=1.0/60.0

fix_dur = 0.2 
image_dur = 0.1 
text_dur = 0.2 

fix_frames = int(fix_dur / refresh) #whole number
image_frames = int(image_dur / refresh) #whole number
text_frames = int(text_dur / refresh) #whole number
total_frames = int(fix_frames + image_frames + text_frames)

stims = ['face01.jpg','face02.jpg','face03.jpg'] 
nTrials=3 
nBlocks=2
my_image = visual.ImageStim(win,units="pix",size=(400,400))

trial_timer = core.Clock() 
block_timer = core.Clock()

for frameN in range(total_frames):
    if 0 <= frameN <= fix_frames:
        win.flip()

        if frameN == fix_frames:
            print("End fix frame =", frameN)

    if fix_frames < frameN <= (fix_frames+image_frames):
        win.flip()

        if frameN == (fix_frames+image_frames):
            print("End image frame =", frameN)

    if (fix_frames+image_frames) < frameN < total_frames:
        win.flip()

        if frameN == (total_frames-1):
            print("End text frame =", frameN)

win.close()