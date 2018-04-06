file = open('file_write.txt', 'r')

print("File contents: ")
for i in file:
    print(i)

file = open('file_write.txt', 'a')

str = input("Enter the text to append to the file: ")
file.writelines(str)

file = open('file_write.txt', 'r')
print('File contents after appending: ')
for i in file:
    print(i);