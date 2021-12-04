

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

l = []
for i in range(len(nums1)):
    if nums1[i] in nums2:
        l.append(nums1[i])
        del nums2[nums2.index(nums1[i])]
print(l)
