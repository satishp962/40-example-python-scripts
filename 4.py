num = int(input("Enter an integer: "))

root = None

for i in range(num):
    if i*i == num:
        root = i

if root is not None:
    pwr = None
    for i in range(1, 6):
        if root**i == num:
            pwr = i

    print("Root:", str(root) + ", Power:", str(pwr))
