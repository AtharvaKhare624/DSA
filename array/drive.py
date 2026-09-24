nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
i = 0
j = 0
while i < m+n:
    if nums2[j] < nums1[i]:
        nums1[i],nums2[j]=nums2[j],nums1[i]

    elif nums1[i] == 0:
        nums1[i],nums2[j]=nums2[j],nums1[i]

        j+=1
    i+=1
print(nums1)