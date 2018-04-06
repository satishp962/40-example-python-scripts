binary = input("Enter the binary of a number: ")

binary = binary[::-1]

sum = 0
for i in range(len(binary)):
    calc = int(binary[i]) * (2**i)
    sum += calc

print("Decimal number is:", sum)
