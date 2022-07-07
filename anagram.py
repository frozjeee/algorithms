def anagram(s, t):
    dct = {}
    if len(s) == len(t):
        for i in range(len(s)):
            if s[i] in dct:
                dct[s[i]] += 1
            else:
                dct[s[i]] = 1
    
        for i in range(len(t)):
            if t[i] in dct:
                dct[t[i]] -= 1
                if dct[t[i]] == 0:
                    dct.pop(t[i])
        return not dct
    return  False

print(anagram("a", "ab"))