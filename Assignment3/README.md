This is my set of answers to Assignment 3:

# Variable Operations Exercise

1. Only subnr_str should be able to work with sub_code because they are both strings. Subnr_int doesn't work because it is a different type of variable compared to sub_code.
2. 
#sub 2

`print (sub_code + " " + subnr_str)`

#sub 222

`print(sub_code + " " + (subnr_str*3))`

#sub2sub2sub2

`print((sub_code + subnr_str)*3)`

#subsubsub222

`print((sub_code*3) + (subnr_str*3))`

# List operations exercise

2. In the list, the list is doubled. So, this meanss that the whole list gets multiplied by the number. In an arraay, each number is doubled. Which means the multiplication affects each number in the array.
3.


#['dodo','rere','mimi','fafa']

`
print([strlist[0]*2,strlist[1]*2,strlist[2]*2,strlist[3]*2])`

#['do','re','mi','fa','do','re','mi','fa']

`print(strlist*2)`

#['do','do','re','re','mi','mi','fa','fa']

`print([strlist[0],strlist[0],strlist[1],strlist[1],strlist[2],strlist[2],strlist[3],strlist[3]])`

#[['do','do'],['re','re'],['mi','mi'],['fa','fa']]

`print([[strlist[0],strlist[0]],[strlist[1],strlist[1]],[strlist[2],strlist[2]],[strlist[3],strlist[3]]])
`

# Zipping Exercises

1. See zippingexample.py


# Indexing Exercises

2. 
`print(colors[-2])
`

3.
print(colors[-2][2])

print(colors[-2][3])

4. 
colors[-1]='indigo'

colors.append('violet')

print(colors)


# Slicing Exercises

2.
`print(list100[:10])`


3.
temp=list100[1::2]

print(temp[::-1])

4.
temp=list100[-4:]

print(temp[::-1])

5.

`print(list100[39:44]==[39,40,41,42,43])`

Yes, they are the same
