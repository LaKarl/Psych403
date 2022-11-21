from psychopy import gui
from datetime import datetime
#=====================
#COLLECT PARTICIPANT INFO
#=====================
#-create a dialogue box that will collect current participant number, age, gender, handedness
exp_info = {'subject_nr':0, 'age': 0, 'handedness':('right','left','ambi'), 
            'gender': '', 'session': 1}
my_dlg = gui.DlgFromDict(dictionary=exp_info,
                         title="subject info",
                         fixed='session', 
                         order=['session', 'subject_nr', 'age', 'gender', 
                                'handedness'],
                         show=False)
#get date and time
date = datetime.now()
#-create a unique filename for the data
exp_info['date'] = str(date.day) + str(date.month) + str(date.year)
print (exp_info['date'])
filename = str(exp_info['subject_nr']) + "_" + exp_info['date'] + '.csv'