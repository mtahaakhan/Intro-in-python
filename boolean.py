# A student makes honour roll if their average is >= 85
# and their lowest grade should be greater than or equals to 70
gpa = float(input('What was your Grade Point Average: '))
lowest_grade = float(input('What was your lowest grade: '))

# You can also use boolean values
if gpa >= 85 and lowest_grade >= 70: # If this is true. Honour roll will be true: Then it will print the command in line 11. If it is honour roll is false, the condition is not matched and it won't show anything
    honour_roll = True
else:
    honour_roll = False    

if honour_roll:
    print('You made honour roll')

    