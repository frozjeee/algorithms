stack = []
st = "()([]"

def isBalanced(stack ,st):
    for ch in st:
        if ch in ["(", "["]:
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if (top == "[" and ch != "]") or (top == "(" and ch != ")"):
                return False
    print(stack)
    return not stack

print(isBalanced(stack, st))