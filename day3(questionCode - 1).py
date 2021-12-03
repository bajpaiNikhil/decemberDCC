

nums = [2, 7, 11, 15]
target = 9
dictionary = {}
for i in range(len(nums)):
    suum = target - nums[i]

    if suum in dictionary:
        print( [dictionary[suum] , i])
    else:
        dictionary[nums[i]] = i
print(dictionary)

