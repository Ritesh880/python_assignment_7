'''2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division'''
a = int(input("enter value of a "))
b = int(input('enter value of  b '))
choice = int(input("enter your choice from 1-4 \n "))
print('')
match choice:
    case 1:
        add = a+b
        print("addition of a and b is ", add)
    case 2:
        sub = a-b
        print("subtraction of a and b is ", sub)
    case 3:
        multi = a*b
        print("multiplication of a and b is ", multi)
    case 4:
        div = a/b
        print("division of a and b is ", div)
      
