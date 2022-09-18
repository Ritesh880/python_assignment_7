# testing negative odd number
x = int(input("enter a number "))
if x % 2 != 0 and x < 0:
    print("negative odd number ")
elif x % 2 != 0 and x > 0:
    print("positive odd number ")
else:
    print("even number ")