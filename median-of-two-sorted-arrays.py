# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

def findMedianSortedArrays(nums1, nums2):
    l = len(nums1) + len(nums2)
    d = 0
    while d < (l - 1) // 2:
        if nums1 == []:
            del nums2[0]
        elif nums2 == []:
            del nums1[0]
        elif nums1[0] > nums2[0]:
            del nums2[0]
        else:
            del nums1[0]
        d += 1

    if l % 2:
        if not nums1:
            return nums2[0]
        if not nums2:
            return nums1[0]
        return nums1[0] if nums1[0] < nums2[0] else nums2[0]

    if not nums1:
        smallest = nums2[:2]
    elif not nums2:
        smallest = nums1[:2]
    elif len(nums1) == 1 and len(nums2) == 1:
        smallest = [nums1[0], nums2[0]]
    elif len(nums1) == 1:
        smallest = [nums2[0], nums1[0] if nums1[0] < nums2[1] else nums2[1]]
    elif len(nums2) == 1:
        smallest = [nums1[0], nums2[0] if nums2[0] < nums1[1] else nums1[1]]
    else:
        smallest = sorted([nums1[0], nums1[1], nums2[0], nums2[1]])[:2]

    return (smallest[0] + smallest[1])/2


print(findMedianSortedArrays([], [2, 3]))
