import re

file = open('31.txt', 'r')

for i in file:
    searchObj = re.search( r'[0-9]{2}-[0-9]{2}-[0-9]{4}', i, re.I|re.M)
    searchObj1 = re.search( r'[\w]*', i, re.I|re.M)
    print("Name:", searchObj1.group() + ", DOB: " + searchObj.group())