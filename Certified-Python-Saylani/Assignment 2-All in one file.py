username = input('Enter your name: ')
print('Welcome ',username,' I hope you are having a great day! There are some questions below. Answer them to see the results. Thanks!')

# 1. Write a program which takes 5 inputs from user for different subject’s marks, total it and generate mark sheet using grades ? 
sub1 = int(input("Enter marks of first subject: "))
sub2 = int(input("Enter marks of second subject: "))
sub3 = int(input("Enter marks of third subject: "))
sub4 = int(input("Enter marks of fourth subject: "))
sub5 = int(input("Enter marks of fifth subject: "))
average=(sub1+sub2+sub3+sub4+sub5)/5

if (average>=90):
    print("Your Grade is: A+")
elif (average>=80):
    print("Your Grade is: A")
elif (average>=70):
    print("Your Grade is: B")
elif (average>=60):
    print("Your Grade is: C")
elif (average>=50):
    print("Your Grade is: D")
elif (average>=33):
    print("Your Grade is: E")
else:
    print("Your Grade is: F")

# 2. Write a program which take input from user and identify that the given number is even or odd? 
 
i = int(input("Enter a number to check if it is an odd or even number: "))
if (i%2==0):
    print(i,"is Even Number")
else:
    print(i, "is Odd Number") 

# 3. Write a program which print the length of the list? 

list = ['Taha','Umair','Anas','Hamza','Basharat','Daniyal']
print("Length of list is: ",len(list), list)
 
# 4. Write a Python program to sum all the numeric items in a list? 

num = [45,97,25,364,46]
total = sum(num)
print('Sum of the list is: ',total)
 
# 5. Write a Python program to get the largest number from a numeric list. 

max_num = [5,6,8,99,22,73,357,1,373,3,136,8,31,367,13,67,7,63,543,43,464,32,368,743,0,641,351,68,4,131,684,31,16,84,31,368,3,13,1,34,684,3,0,743,1,384,3,1337,51,684,3,13,13]
check = max(max_num)
print('Largest number in the list is: ',check)
 
# 6. Take a list, say for example this one: 
#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
# and write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i <= 5:
        print(i, ' less than 5')
    


