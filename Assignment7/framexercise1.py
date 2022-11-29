from psychopy import visual, monitors, event, core

#define the monitor parameters
mon = monitors.Monitor('myMonitor', width=35.56, distance=60)
mon.setSizePix([1600,900])
win = visual.Window(monitor=mon)

#set durations
fix_dur = 0.2 #200 ms
image_dur = 0.1 #100 ms
text_dur = 0.2 #200 ms

#set frame counts
fix_frames = int(fix_dur / refresh) #whole number
image_frames = int(image_dur / refresh) #whole number
text_frames = int(text_dur / refresh) #whole number
#the total number of frames to be presented on a trial
total_frames = int(fix_frames + image_frames + text_frames)

fix = visual.TextStim(win, text='+')

nBlocks=1
nTrials=1

for block in range(nBlocks):
    #=====================
    #TRIAL SEQUENCE
    #=====================    
    for trial in range(nTrials):
        #-set stimuli and stimulus properties for the current trial
        
        
        #=====================
        #START TRIAL
        #=====================   
        for frameN in range(total_frames): #for the whole trial...
            #-draw stimulus
            if 0 <= frameN <= fix_frames: #number of frames for fixation      
                fix.draw() #draw
                win.flip() #show
                
                if frameN == fix_frames: #last frame for the fixation
                    print("End fix frame =", frameN) #print frame number
                    
            #number of frames for image after fixation
            if fix_frames < frameN <= (fix_frames+image_frames):      
                fix.draw() #draw
                win.flip() #show 
                
                if frameN == (fix_frames+image_frames): #last frame for the image
                    print("End image frame =", frameN) #print frame number  
                    
            #number of frames for the final text stimulus    
            if (fix_frames+image_frames) < frameN < total_frames:  
                fix.draw() #draw
                win.flip() #show  
                
                if frameN == (total_frames-1): #last frame for the text
                    print("End text frame =", frameN) #print frame number    
win.close()