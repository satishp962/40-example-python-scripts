x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
z = int(input("Enter number 3: "))

if x%2 != 0:
    if y%2 != 0:
        if z%2 != 0:
            if x > y:
                if x > z:
                    print("x is greater.")
                else:
                    print("z is greater.")
            else:
                if y > z:
                    print("y is greater.")
                else:
                    print("z is greater.")
        else:
            if x > y:
                print("x is greater.")
            else:
                print("y is greater.")
    else:
        print("x is greater.")
else:
    if y%2 != 0:
        if z%2 != 0:
            if y > z:
                print("y is greater.")
            else:
                print("z is greater.")
        else:
            print("y is greater.")
    elif z%2 != 0:
            print("z is greater.")
    else:
        print("No odd numbers.")
            
