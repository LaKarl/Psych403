from psychopy import gui

exp_info = {'subject_nr':0, 'age': 0, 'handedness':('right','left','ambi'), 
            'gender': '', 'session': 1}

my_dlg = gui.DlgFromDict(dictionary=exp_info,
                         title="subject info",
                         fixed='session', 
                         order=['session', 'subject_nr', 'age', 'gender', 
                                'handedness'],
                         show=False)

print("All variables have been created! Now ready to show the dialog box!")

my_dlg.show()