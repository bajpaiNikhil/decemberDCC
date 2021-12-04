prices = [7,1,5,3,6,4]

low = float('inf')
profit = 0
for i in prices:
    profit = max(profit, i - low)
    low = min(low, i)
print(profit)