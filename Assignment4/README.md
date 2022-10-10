This is my set of answers to Assignment 4:

### Conditional Exercises

1.

```python
response = input("1 or 2")
if response=='1' or response=='2':
    print('OK')

elif response=='':
    print('The subject did not respond')

else:
    print('The subject pressed the wrong key')
```

2.
```python
response = input("1 or 2")
if response=='1' or response=='2':
    if response=='1':
        print("Correct")
    if response=='2':
        print("Incorrect")

elif response=='':
    print('The subject did not respond')

else:
    print('The subject pressed the wrong key')
 ```
3. Yes it does

### For Loop Exercise
1. 
```python
name = "Karl"
for letter in name:
    print(letter)
```

2.
```python
name = "Karl"
counter = -1
for letter in name:
    counter +=1
    print(name[counter])
```

3.
```python
names = ["Amy","Rory", "River"]
for name in names:
    for letter in name:
        print(letter)
```
4.
```python
names = ["Amy","Rory", "River"]
for name in names:
    counter = -1
    for letter in name:
        counter += 1
        print(letter)
        print("Index at: " + str(counter))
```
### While loop Exercise
1.
```python
iteration=0
while iteration<20:
    if iteration<10:
        print('%i:image1.png'%iteration)
    elif iteration<20:
        print('%i:image2.png'%iteration)
    iteration+=1
```

2.
```python
import random

response=None
while response != "1" and response != "2":
    images=random.randint(0,10)
    print('randomimage'+str(images))
    response = input()
```
3.
```python
import random
failsafe = 5
response=None
while response != "1" and response != "2" and failsafe !=0:
    images=random.randint(0,10)
    print('randomimage'+str(images))
    response = input()
    failsafe-=1
```
