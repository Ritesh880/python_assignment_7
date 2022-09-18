'''7. Write a python program to check whether a given number is positive, negative or
zero using match case statement'''

x = int(input("enter a numner"))
match x:
    case x if x>0:
        print("Positive number")
    case x if x<0:
        print("Negative number ")  
    case x if x==0:
        print("zero ")      