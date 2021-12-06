



from collections import Counter

position = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]


odd_parity = 0
even_parity = 0

for i in position:
    if i%2 == 0:
        even_parity +=1
    else:
        odd_parity +=1
print(min(odd_parity , even_parity))