#Looping through a string
for x in "Collins Oduor":
    print(x)

#Determining the position of a char
x = 'Collins Oduor'
print(x[0], x[8], x[12])

#To determine if a word is present in a string (`in` is used) returns true if the word is present
x = "I am learning python"
if 'python' in x:
    print("Python is present")
#`not in` is used to reverse the effect of `in` i.e by returning true if the word is absent
x = 'Glad to have learnt C programming'
if 'python' not in x:
    print("Python is absent")
else:
    print('Python is present')

#To determine the length of a string, `len()` is used
x = 'Collins'
y= len (x) #The value returned will be 7
print(y)

#String slicing i.e returning string from a certain range, the first value is the the start value followed by colon then the end value
#note that range begin from 0
x ='Collins'
print(x[1:6])#output is ollin
#slicing can also be done reversely by using negative(-ve) index values
x='Collins'
print(x[-4:-1]) #output os 'lin'