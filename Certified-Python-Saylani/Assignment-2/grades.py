# Question 1
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


