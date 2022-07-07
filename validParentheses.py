def valid(s):
    arr = []
    for i in s:
        if i in ["(", "{", "["]:
            arr.append(i)
        else:
            if not arr:
                return False
            else:
                if i == ")" and arr[-1] != "[" and arr[-1] != "{":
                    arr.pop()
                elif i == "]" and arr[-1] != "(" and arr[-1] != "{":
                    arr.pop()
                elif i == "}" and arr[-1] != "[" and arr[-1] != "(":
                    arr.pop()
                else:
                    return False
    return not arr

print(valid("]"))