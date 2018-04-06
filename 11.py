count = 0

def rec_fib(num):
    if num == 1:
        return 1
    elif num == 2:
        global count
        count = count + 1
        return 1
    else:
        return (rec_fib(num - 1) + rec_fib(num - 2))

print('fib(8) is : ' + str(rec_fib(8)))
print('No. of times fib(2) is calculated: ' + str(count))