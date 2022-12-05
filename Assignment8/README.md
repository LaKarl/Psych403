
## PsychoPy Keypress Exercise

1. See [keypress1](https://github.com/LaKarl/Psych403/blob/main/Assignment8/keypress1.py) here.
2. If we call the function within the trial loop, the keys will be cleared every trial. Which is the desired effect. However, if we call it outside of the function, the keys won't be cleared after each trial, so all keys that are pressed since the first trial will be stored, which is not what we want. If you unindent the if keys line, it will print out the last trial's first key only.

## Recording data exercises
1. 
```python
my_dict = {"KeyName":[],"SubRT":[],"SubAcc":[],"CorrResp":[]}

my_dict["KeyName"].append()
my_dict["SubRT"].append()
my_dict["SubAcc"].append()
my_dict["CorrResp"].append()
```

2. See [Recording data2](https://github.com/LaKarl/Psych403/blob/main/Assignment8/RecordingData.py) here. 
## Save csv exercises
```python
with open('saved_csv.csv', 'w') as f:
    fieldnames = ['block', 'trial', 'prob','corr_resp','sub_resp','sub_acc', 'resp_time']
    data_writer = csv.DictWriter(f, fieldnames=fieldnames)
    data_writer.writeheader()
    for result in results:
       print(result)
       data_writer.writerow(result)
```
## Save JSON exercises

#Read Json exercises
