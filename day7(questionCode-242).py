from collections import Counter

s = "a"
t = "n"

d1 = dict(Counter(s))
d2 = dict(Counter(t))

if(d1 == d2):
    print(True)
else:
    print(False)