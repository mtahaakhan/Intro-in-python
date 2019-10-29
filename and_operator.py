# A student makes honour roll if their average is >= 85
# and their lowest grade should be greater than or equals to 70

gpa = float(input('What was your Grade Point Average: '))
lowest_grade = float(input('What was your lowest grade: '))

# 1st way of doing it (This is Nested if)

if gpa >= 85:
    if lowest_grade >= 70:
        print('Well done')

# 2nd way of doing it (This is AND Operator)

if gpa >= 85 and lowest_grade >= 70:
    print('Well done')        

# 2nd way is better because it's more clean
