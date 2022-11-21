from psychopy import visual, monitors
#=====================
#CREATION OF WINDOW AND STIMULI
#=====================
#-define the monitor settings using psychopy functions
mon = monitors.Monitor('myMonitor', width = 35.56, distance = 60)
mon = setSizePix([1600,900])
mon.save()
#-define the window (size, color, units, fullscreen mode) using psychopy functions
win = visual.Window(monitor=mon, size=(800,800), color=(-1,-1,-1), units ='None', fullscr =False,)
