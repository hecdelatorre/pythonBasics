x = 30

if x < 30:
    print("x is less than 30")
elif x == 30:
    print("x is 30")  
else:
    print("x is greater than 30")
    
color = "blue"
if color == "blue":
    print("any color")
    
name = "John"
lastName = "Carter"

if name == "John":
    if lastName == "Carter":
        print("You are John Carter")
    else:
        print("You are not John")
else:
    print("You are not John Carter")
    
y = 10
if y > 2 and y <= 10: # Operadores logicos, and, or, not
    print("y is greater than two and less than or equal to ten")
    
if(not(x == y)):
    print("x is not equal y")