nums = input("Enter the string: ")

sum = 0
num = ''
for i in nums:
    if i != ',':
        num += i
    else:
        sum += float(num)
        num = ''

sum += float(num)

print("Sum of the decimals in the string is:", float(sum))