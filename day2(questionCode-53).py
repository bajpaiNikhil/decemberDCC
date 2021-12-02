nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

currentMax = globalMax = nums[0]

for i in range(1,len(nums)):
    currentMax = max(nums[i], currentMax + nums[i])
    if currentMax > globalMax:
        globalMax = currentMax
print(globalMax)
