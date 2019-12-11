# # Question 1 : Write a Python function to calculate the factorial of a number (a non-negative
# # integer). The function accepts the number as an argument.

def is_positive_integer(num):
    if int(num) > 0 :
        return True
    else:
        return False
def calculate_factorial(num):
    factorial = 1
    if is_positive_integer(num) == True:
        num = int(num)
        for i in range(1, num + 1):
            factorial = factorial * i
        print(factorial)
    else:
        print("Invalid input")

factorial_calculation = input("Enter Number to calculate it's factorial: ")
calculate_factorial(factorial_calculation)


# # Question:2
# # Write a Python function that accepts a string and calculate the number of upper
# # case letters and lower case letters.

def counter(string):
    upper=0
    lower=0
    for x in string:
        if x >= 'A' and x <= 'Z':
            upper +=1
        elif x >= 'a' and x <= 'z':
            lower +=1 
    print('Upper case: ', upper)
    print('Lower case: ', lower)

string = input('Enter String:')
# counter(string)

# Question:3
# Write a Python function to print the even numbers from a given list.


List = [2, 3, 23, 54, 45, 23, 78, 56, 99, 24]
for element in List:
    if element % 2 == 0:
        print(element)

# Question:4
# Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same
# backward as forward, e.g., madam

def check(string):
    if(string == string[::-1]):
        print('The string is a palindrome')
    else:
        print('Not a palindrome')
string = input('Etner word to check is it Palindrome: ')
check(string)

# Question:5
# Write a Python function that takes a number as a parameter and check the
# number is prime or not.


number = int(input('Enter num to check it is prime or not: '))
def prime(number):
    if number > 1:
        for i in range(2, number // 2):
            if(number % i)==0:
                print(number, ' is not a prime')
                break
            else:
                print(number, 'is a prime number ')
    else:
        print(number, 'is not a prime number')

prime(number)

# Question: 6
# Suppose a customer is shopping in a market and you need to print all the items
# which user bought from market.
# Write a function which accepts the multiple arguments of user shopping list and
# print all the items which user bought from market.
# (Hint: Arbitrary Argument concept can make this task ease)

def shopping(*items):
    shopping_items = []
    while True:
        item = input("Enter Shopping item [-1 to abort]: ")
        if item != '-1':
            shopping_items.append(item)
        else:
            break
    for item in range(len(shopping_items)):
        print("You purchased: {}".format(shopping_items[item]))
shopping()
