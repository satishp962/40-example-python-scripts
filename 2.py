largest_odd = 1

for i in range(10):
    num = int(input("Enter the number: "))

    if num > 1 and num%2 != 0 and num > largest_odd:
        largest_odd = num
    
print("Largest odd number is:", largest_odd)
