num = int(input("Enter the no. of lines: "))

half = num // 2

for p in range(half):
    print('*', end='')

    for l in range(num):
        print(' ', end='')

    print('*')

for i in range(half):
    for j in range(half - i):
        if j==0:
            print('*', end='')
        else:
            print(' ', end='')

    print('*', end='')

    if i != 0:
        for k in range(i):
            print(' ', end='')

    for j in range(i, 0, -1):
        print(' ', end='')

    print('*', end='')

    for j in range(half - i - 1):
        print(' ', end='')

    print('*')
    

    







        
        
