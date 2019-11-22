#  Write a Python program to sum all the numeric items in a dictionary 

sum_dictionary = {'num1':4,'num2':3,'num3':3}

# Adding another key into dictionary

sum_dictionary['num4']=15

total = sum(sum_dictionary.values())
print('Sum of all the numeric items in a dictionary is: ',total)