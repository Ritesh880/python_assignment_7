'''10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday'''

fav_colour = input("Enter your fav_colour ")

match fav_colour:
    case fav_colour if "yellow" in fav_colour:
        print("Monday")
    case fav_colour if "blue " in fav_colour:
        print("Tuesday")
    case fav_colour if "orange" in fav_colour:
        print("Wednesday")
    case fav_colour if "white" in fav_colour:
        print("Thrusday")
    case fav_colour if "black " in fav_colour:
        print("Friday")
    case fav_colour if "red" in fav_colour:
        print("Saturday")
    case fav_colour if fav_colour != "yellow"and"blue"and"orange"and"white"and"black"and"red":
        print("sunday")
