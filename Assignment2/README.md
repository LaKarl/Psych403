This is my set of answers to Assignment 2:

Print Exercises
1. 
2. No variables show up in the variable editor

Operation Exercises
1. Yes, python outputs the same value at 2.5 for both of these formats. 
2. The modulo operator outputs the remainder of an integer division.
3. ** represents the exponentation operator and it puts the second number as the exponent on the first number. For instance, 9**4 is the same as 9^4. On the other hand // is the operation for floor division, which is basically just the first part of the modulo, so it just divides and discards the remainder.
4. Yes, python follows order of operations

Variable Exercises
2. Yes, variables show up in the variable editor now.
3. No, python does not have any problem with 2 ore more different variables having the same value
5. No, changing the value of letterx does not change the value of the other value that had the same value of letterx before it was changed. Only letterx was changed.
6. No, letterx stayed the same when performing the exercise in this order. This tells us that python variable assignment works on a line to line basis.

Boolean exercises
1. 1 and 1.0 are equivalent because Python doesn't require that 2 items be the same type to consider them equal. However, "1" and "1.0" are no equivalent because they are both strings and the strings are not the same as each other. For instance, it doesn't even view the numbers as numbers the same way it would if it was an integer or a float.
2. Yes
3. 
`print(1 == 1.0 and not "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 or "1" == "1.0" or 5 == (3+2))
print(1 == 1.0 and not "1" == "1.0" and 5 == (3+2))
print(1 == 1.0 and not "1" == "1.0" or 5 == (3+2))`

List Exercises
1. Yes, oddlist became a variable.
3. It says 5
4. Python calls oddlist a list
5. `intlist = list(range(0, 101))`
6. Yes

Dictionary Exercise
1.
`about me = {
'name': 'Karl',
'age': 21.0,
'year': 4
'Favorite foods': ['Sushi', 'Pizza', 'Burritos'],
}`
