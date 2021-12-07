
from collections import Counter

s = "loveleetcode"

d = dict(Counter(s))

for key,val in d.items():
    if val == 1:
        print(s.index(key))
        break
