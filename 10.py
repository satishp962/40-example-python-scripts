# iterative factorial
def iter_fact(num):
    ans = 1
    while num >= 1:
        ans = ans * num
        num = num - 1

    return ans

print(iter_fact(5))        

# recursive factorial
def rec_fact(num):
    if num == 1:
        return 1
    else:
        return num * rec_fact(num - 1)

print(rec_fact(5))        

# iterative fibonacci
def iter_fib(num):
    a = 1
    b = 1
    
    if num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    else:
        c = 0
        ans_list = [1, 1]
        for _ in range(num):
            c = a + b
            a = b
            b = c
            ans_list.append(c)
        
        return ans_list

print(iter_fib(5))

# recursive fibonacci
def print_rec_fib(num):
    
    def rec_fib(num):
        if num == 1:
            return 1
        elif num == 2:
            return 1
        else:
            return (rec_fib(num - 1) + rec_fib(num - 2))
    
    fibs = []
    for _ in range(num + 1):
        fibs.append(rec_fib(_ + 1))

    print(fibs)


print_rec_fib(10)

# iterative palindrome
def iter_pal(str):
    i = 0
    j = len(str) - 1

    ans = None
    if len(str) == 1:
        ans = True
    elif len(str) == 2:
        if str[0] == str[1]:
            ans = True
        else:
            ans = False
    else:
        while i != j:
            if str[i] == str[j]:
                i = i + 1
                j = j - 1

                ans = True
                continue
            else:
                ans = False
                break

    return ans

print(iter_pal('ab'))

# recursive palindrome
def ispalindrome1(word):
    return word == word[::-1]

def ispalindrome(word):
    if len(word) < 2: 
        return True

    if word[0] != word[-1]: 
        return False
        
    return ispalindrome(word[1:-1])

print(ispalindrome('aba'))
print(ispalindrome('aaca'))
        