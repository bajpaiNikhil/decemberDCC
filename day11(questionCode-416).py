nums = [1, 2,3,5]


totalSum = sum(nums)
d = {0}
f = totalSum // 2
print(f ,11)
for i in range(len(nums)-1):
    for j in range(len(d)):
        print(d[nums[j]])
        d.add(nums[i] )

print(d)
print(f in d)
