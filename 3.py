num = int(input("Enter the integer value: "))

for i in range(num):
    if i**3 == num:
        yes = True
        break
    else:
        yes = False

if yes:
    print("The given number is a perfect cube of", str(i) + ".")
else:
    print("The given number is not a perfect cube.")
