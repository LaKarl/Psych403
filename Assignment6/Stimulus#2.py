from psychopy import visual, monitors, event
import os
import numpy as np

mon = monitors.Monitor('myMonitor', width = 13.5, distance = 60)
mon.setSizePix([3000,2000])
win = visual.Window(monitor=mon, size=(800,800), color=(-1,-1,-1))

os.chdir('/Pictures')
main_dir = os.getcwd() 
image_dir = os.path.join(main_dir,'images')

face1 = visual.ImageStim(win, units='pix',image='/Pictures/image/face01.jpg',pos=(200,100), size=(400,400))
face2 = visual.ImageStim(win,units='pix',image='/Pictures/image/face02.jpg',pos=(-200,100), size=(400,400))
face3 = visual.ImageStim(win, units='pix',image='/Pictures/image/face03.jpg',pos=(-200,-100), size=(400,400))
face4 = visual.ImageStim(win, units='pix',image='/Pictures/image/face04.jpg',pos=(200,-100), size=(400,400))

face1.draw()
win.flip() 
event.waitKeys() 

face2.draw()
win.flip() 
event.waitKeys() 

face3.draw()
win.flip() 
event.waitKeys() 

face4.draw()
win.flip() 
event.waitKeys() 

win.close()