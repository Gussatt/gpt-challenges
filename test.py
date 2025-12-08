def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = m # 3
    j = 0

    len_a = len(nums1)
    len_b = len(nums2)
    print(i)
    while i < len_a and j < len_b :
        nums1[i] = nums2[j]
        i += 1
        j += 1

    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

print(merge(nums1, m, nums2, n))
