nums = [-2, 3, -4]

prefixMax , suffixMax , maxSoFar  = 0, 0, float('-inf')

for i in range(len(nums)):

    prefixMax = (prefixMax or 1) * nums[i]
    suffixMax = (suffixMax or 1) * nums[~i]
    maxSoFar = max(maxSoFar, suffixMax, prefixMax)

    # print(prefixMax, suffixMax, maxSoFar, ~i, i)

print(maxSoFar)

print(bin(12) , bin(1) , bin(2 or 1))



