from psychopy import visual, monitors, event, core
import os
import numpy as np

mon = monitors.Monitor('myMonitor', width = 13.5, distance = 60)
mon.setSizePix([3000,2000])
win = visual.Window(monitor=mon, size=(800,800), color=(-1,-1,-1))

nTrials=3
my_text=visual.TextStim(win)
fix=visual.TextStim(win, text='+')
sub_resp = []
for trial in range(nTrials):
    
    keys = event.getKeys(keyList=['1','2']) #put getkeys HERE
    my_text.text = "trial %i" %trial #insert integer into the string with %i
    
    fix.draw()
    win.flip()
    core.wait(2)
    
    event.clearEvents() #clear events HERE
    
    my_text.draw()
    win.flip()
    core.wait(1)
    
if keys:
    sub_resp = keys[0] #only take first response
        
    print(sub_resp)    
    
win.close()