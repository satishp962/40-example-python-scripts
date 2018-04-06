searchstr = input("Enter the string you want to use: ")
searchstr = [ord(x) for x in searchstr]

def sort(mystr):

    for i in range(len(mystr)):
        key = mystr[i]

        j = i - 1
        while j >= 0 and key < mystr[j]:
            mystr[j+1] = mystr[j]
            j = j - 1
        
        mystr[j+1] = key

sort(searchstr)
searchstr = [chr(x) for x in searchstr]
print(searchstr)