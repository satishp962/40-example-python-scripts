class py_solution:
    def __init__(self):
        print("Object created.")

    def is_valid_parenthese(self, str1):
            stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
            for parenthese in str1:
                if parenthese in pchar:
                    stack.append(parenthese)
                elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                    return False
            return len(stack) == 0

chkcls = py_solution()

print(chkcls.is_valid_parenthese("(){}[]"))
print(chkcls.is_valid_parenthese("()[{)}"))
print(chkcls.is_valid_parenthese("()"))