def isPalindrome(s: str):
    a = 0
    b = len(s) - 1
    while a <= b:
        c = s[a].lower()
        d = s[b].lower()
        if c.isalnum() and d.isalnum() and c == d:
            a += 1
            b -= 1
        elif not s[a].isalnum():
            a += 1
        elif not s[b].isalnum():
            b -= 1
        elif c != d:
            return False
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))