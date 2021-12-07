

ransomNote = "aa"
magazine = "ab"
l=[]

for i in set(ransomNote):
    if(ransomNote.count(i) <= magazine.count(i)):
        l.append(True)
    else:
        l.append(False)
print(all(l))