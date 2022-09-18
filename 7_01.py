'''Write a python script to display the number of days in a given month number.'''
from email.policy import default


a = int(input("enter month"))
match a:
    case 1:
        print("It's JAN so it has 31 days ")
    case 2:
        print("It's FEB so it has 28 days ")
    case 3:
        print("It's March so it has 31 days ")
    case 4:
        print("It's April so it has 30 days ")
    case 5:
        print("It's May so it has 31 days ")
    case 6:
        print("Its June so it has 30 days ")
    case 7:
        print("Its July so it has 31 days ")
    case 8:
        print("Its AUG so it has 31 days")
    case 9:
        print("Its SEP so it has 30 days")

    case 10:
        print("Its OCT so it has 31 days ")
    case 11:
        print("Its NOV so it has 30 days ")
    case 12:
        print("Its DEC so it has 31 days ")
 