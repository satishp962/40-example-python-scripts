# caesor cipher

def encrypt(ip, key):
    output = ''

    for i in range(len(ip)):
        output += key[ord(ip[i]) - 65]

    return str(output)

def decrypt(ip, key):
    output = ''
    
    for i in range(len(ip)):
        output += key[ord(ip[i]) - 65]

    return str(output)

key = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
msg = input("Enter the message you want to encrypt: ")

ciphertext = encrypt(msg, key)
print("Ciphertext is:", ciphertext)

plaintext = decrypt(ciphertext, key)
print("Plaintext is:", plaintext)

