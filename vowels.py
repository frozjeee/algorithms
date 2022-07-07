# a e i o u



# aa ae ai ao au
# ee ei eo eu
# ii io ui
# oo ou
# uu




# aaa aae aai aao aau         eee eei eeo eeu         iii iio iiu         ooo oou         uuu
# aee aei aeo aeu             eio eio eiu             ioo iou             ouu
# aii aio aiu                 eoo eou                 iuu
# aoo aou                     euu
# auu





# aaaa aaae aaai aaao aaau        eeee eeei eeeo eeeu         iiii iiio iiiu          oooo ooou           uuuu
# aaee aaei aaeo aaeu             eeii eeio eeiu              iioo iiou               oouu
# aaii aaio aaiu                  eeoo eeou                   iiuu
# aaoo aaou                       eeuu
# aauu

# aeee aeei aeeo aeeu             eiii eiio eiiu              iooo ioou               ouuu
# aeii aeio aeiu                  eioo eiou                   iouu
# aeoo aeou                       eiuu    
# aeuu

# aiii aiio aiiu                  eooo eoou                   iuuu
# aioo aiou                       eouu
# aiuu

# aooo aoou                       euuu
# aouu

# auuu


#    5  10  15  20  25

#  5  10  20  35  55   80
# 0  5  15  35  70  125
# 0  1   2   3   4
def foo(n):
    count = 0
    mnozh = 0
    for i in range(n + 1):
        count += mnozh      # 0 | 5  | 15 | 35
        if i == 0:
            mnozh += 5   
        else:
            mnozh += 5 * i    # 5 | 10 | 20 | 35
    return count

print(foo(33))