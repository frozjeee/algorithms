from collections import defaultdict


def lengthOfLongestSubstring(s: str) -> int:
    dct = defaultdict(lambda: -1)
    l = 0
    r = 0
    seq = 1
    maxx = 1
    if len(s) == 0:
        return 0
    while r < len(s) - 1:
        dct[s[r]] = r
        print(s[l:r+1])
        print(seq)
        print(dct)

        if dct[s[r]] == -1:
            print(f"---{r}")
            r += 1
            seq += 1
        elif dct[s[r]] != -1:
            print(f"==={r}")
            l += 1
            dct[s[l]] = None
        if maxx < seq:
            maxx = seq
    return maxx


print(lengthOfLongestSubstring("abcabcbb"))