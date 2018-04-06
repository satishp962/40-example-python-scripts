num = int(input("Enter the number you want to search in the list: "))

num_list = [2, 5, 8, 9, 6, 26, 45, 12, 75, 36]

# sequential search
not_avail = False
for i in range(len(num_list)):
    if num == num_list[i]:
        print("Number available in the list.")
        not_avail = False
        break
    else:
        not_avail = True

if not_avail == True:
    print("Number not available in the list.")
        