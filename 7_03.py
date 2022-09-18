'''Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.'''

print("enter three number ")
p = int(input("enter value of p "))
b = int(input("enter value of b "))
h = int(input("enter value of h "))


match (p, b, h):
    case (p, b, h) if p == b:
        print("isoscale triangle")
    case (p, b, h) if h**2 == (p**2+b**2):
        print("right angle triangle")
    case (p, b, h) if p == b == h:
        print("Equilateral triangle ")
