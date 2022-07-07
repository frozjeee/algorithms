def valid(s):
    a = "".join(s[i].lower() for i in range(len(s)) if s[i].isalnum())
    i = 0
    j = len(a) - 1
    while i < j:
        if a[i] != a[j]:
            return False
        i += 1
        j -= 1
    return True


print(valid(" "))

# def isPalindrome(s):
#     s = ''.join(e for e in s if e.isalnum()).lower()
#     return s==s[::-1]


# def isPalindrome(s):
#     l, r = 0, len(s) - 1
#     while l < r:
#         if not s[l].isalnum():
#             l += 1
#         elif not s[r].isalnum():
#             r -= 1
#         else:
#             if s[l].lower() != s[r].lower():
#                 return False
#             else:
#                 l += 1
#                 r -= 1
#     return True