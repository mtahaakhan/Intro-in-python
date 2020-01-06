import turtle


# Here we were making a turtle 
# my_turtle = turtle.Turtle()
# my_turtle.forward(100)
# my_turtle.left(90)      
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)
# my_turtle.left(90)
# my_turtle.forward(100)




# Now we are using function in it



# my_turtle = turtle.Turtle()

# def square():
#     my_turtle.forward(100)
#     my_turtle.left(90)      
#     my_turtle.forward(100)
#     my_turtle.left(90)
#     my_turtle.forward(100)
#     my_turtle.left(90)
#     my_turtle.forward(100)

# square()

# Here we are giving Multiple Function Arguments

my_turtle = turtle.Turtle()

def square(length, deg):
    my_turtle.forward(length)
    my_turtle.left(deg)      
    my_turtle.forward(length)
    my_turtle.left(deg)
    my_turtle.forward(length)
    my_turtle.left(deg)
    my_turtle.forward(length)

square(100, 90)
