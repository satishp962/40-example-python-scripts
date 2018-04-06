dec = int(input("Enter any decimal number: "))
    
def find_octal(num):
    octal = ''
    
    while num > 0:
        x = num//8
        rem = num%8
        num = x

        octal += str(rem)

    return octal[::-1]

def find_hex(num):
    hexa = ''
    
    while num > 0:
        x = num//16
        rem = num%16
        num = x

        if rem > 9:
            rem1 = chr(55 + rem)

        hexa += str(rem1)

    return hexa[::-1]

print("Octal number is:", find_octal(dec))
print("Hexadecimal number is:", find_hex(dec))