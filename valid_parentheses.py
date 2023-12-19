def checkValidString(s):
    arr = []
    cntr = 0
    for i in s:
        if i == "(":
            arr.append(i)
        elif i == "*":
            cntr += 1
        else:
            if not arr:
                return False
            else:
                if i == ")":
                    arr.pop()
                else:
                    return False
    return True if len(arr) - cntr <= 0 else False
