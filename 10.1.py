# character occurence
mystr = input("Enter the string: ")
char_dict = {}

for i in range(len(mystr)):
    count_char = mystr.count(mystr[i])
    char_dict[mystr[i]] = count_char

set(char_dict.keys())

print(char_dict)
