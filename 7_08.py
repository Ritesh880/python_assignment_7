'''Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement'''

str1 = input("enter first string  ")
str2 = input("enter second string ")
match (str1,str2):
    case (str1,str2) if str1==str2:
        print("identical")
    case (str1,str2) if str1>str2:
        print(str2,str1)
    case(str1,str2) if str2>str1:
        print(str1,str2)        
  