def IsIn(str1, str2):
    if str1 in str2 or str2 in str1:
        return True
    else:
        return False

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

print(IsIn(str1, str2))