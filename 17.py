num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

def find_common_factor(num1, num2):
    common = ()
    for i in range(1, min(num1, num2) + 1):
        if num1%i == 0 and num2%i == 0:
            common = common + (i,)

    min_fac = min(common)
    max_fac = max(common)
    
    fac_sum = 0
    for _ in range(len(common)):
        fac_sum += int(common[_])

    return (min_fac, max_fac, fac_sum, common)

min_f, max_f, sum_fac, facs = find_common_factor(num1, num2)

print("Factors:", facs)
print("Minimum:", min_f, "\nMaximum:", max_f, "\nSum of the factors:", sum_fac)