from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        print(nums1)
        print(nums2)
        total_count = len(nums1) + len(nums2)
        # if total_count % 2 == 0:
        #     median_idx = (total_count / 2, total_count / 2 - 1)
        # else:
        median_idx = total_count // 2
        print(f'median_idx:{median_idx}')

        nums1_high_idx = len(nums1) - 1
        nums1_low_idx = 0
        nums2_high_idx = len(nums2) - 1
        nums2_low_idx = 0

        for _ in range(100):
            print()
            nums1_mid_idx = (nums1_high_idx + nums1_low_idx) // 2
            nums1_mid_val = nums1[nums1_mid_idx]

            nums2_mid_idx = (nums2_high_idx + nums2_low_idx) // 2
            nums2_mid_val = nums2[nums2_mid_idx]
            print(
                f'nums1_low_idx: {nums1_low_idx}, nums1_mid_idx: {nums1_mid_idx}, nums1_high_idx: {nums1_high_idx}')
            print(
                f'nums2_low_idx: {nums2_low_idx}, nums2_mid_idx: {nums2_mid_idx}, nums2_high_idx: {nums2_high_idx}')

            print(f'nums1_mid_val: {nums1_mid_val}')
            print(f'nums2_mid_val: {nums2_mid_val}')

            if nums1_mid_val <= nums2_mid_val:
                print('nums1_mid_val <= nums2_mid_val')
                nums_lower_than_2 = nums1_mid_idx + nums2_mid_idx + 1
                print(f'nums_lower_than_2: {nums_lower_than_2}')
                nums1_higher = len(nums1) - nums1_mid_idx - 1
                nums2_higher = len(nums2) - nums2_mid_idx - 1
                nums_higher_than_1 = nums1_higher + nums2_higher + 1
                print(f'nums_higher_than_1: {nums_higher_than_1}')

                # Check if nums1 is median here
                low_cut = nums2_low_idx
                high_cut = len(nums2) - nums2_mid_idx
                # print('high_cut', high_cut)
                # print('low_cut', low_cut)
                if nums1_mid_idx + low_cut == median_idx and high_cut + len(nums1) - nums1_mid_idx - 1 == median_idx:
                    return nums1_mid_val

                # Check if nums2 is median here
                low_cut = nums1_mid_idx + 1
                high_cut = len(nums1) - nums1_high_idx - 1
                print('high_cut', high_cut)
                print('low_cut', low_cut)
                if nums2_mid_idx + low_cut == median_idx and high_cut + len(nums2) - nums2_mid_idx - 1 == median_idx:
                    return nums2_mid_val

                # Too low, raise nums1
                elif nums_higher_than_1 > median_idx:
                    print('raise nums1')
                    nums1_low_idx = nums1_mid_idx + 1
                # Too high, lower nums2
                elif nums_lower_than_2 > median_idx:
                    nums2_high_idx = nums2_mid_idx - 1
                    print('lower nums2')

            # Invert logic
            elif nums1_mid_val > nums2_mid_val:
                print('nums2_mid_val > nums1_mid_val')
                nums_lower_than_1 = nums2_mid_idx + nums1_mid_idx + 1
                print(f'nums_lower_than_1: {nums_lower_than_1}')
                nums2_higher = len(nums2) - nums2_mid_idx - 1
                nums1_higher = len(nums1) - nums1_mid_idx - 1
                nums_higher_than_2 = nums2_higher + nums1_higher + 1
                print(f'nums_higher_than_2: {nums_higher_than_2}')

                # Check if nums1 is median here
                low_cut = nums2_mid_idx + 1
                high_cut = len(nums2) - nums2_high_idx - 1
                if nums1_mid_idx + low_cut == median_idx or high_cut + len(nums1) - nums1_mid_idx - 1 == median_idx:
                    return nums1_mid_val

                # Check if nums2 is median here
                low_cut = nums1_low_idx
                high_cut = len(nums1) - nums1_high_idx
                if nums2_mid_idx + low_cut == median_idx or high_cut + len(nums2) - nums2_mid_idx - 1 == median_idx:
                    return nums2_mid_val

                # Too low, raise nums1
                elif nums_higher_than_1 > median_idx:
                    print('raise nums1')
                    nums1_low_idx = nums1_mid_idx + 1
                # Too high, lower nums2
                elif nums_lower_than_2 > median_idx:
                    nums2_high_idx = nums2_mid_idx - 1
                    print('lower nums2')


print(Solution().findMedianSortedArrays([1, 2, 3, 4, 5, 6], [4, 5, 7, 8, 11]))
