class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        print(nums1)
        print(nums2)
        total_count = len(nums1) + len(nums2)
        # if total_count % 2 == 0:
        #     median_idx = (total_count / 2, total_count / 2 - 1)
        # else:
        median_idx = int(total_count / 2)
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
            print(f'nums1_low_idx: {nums1_low_idx}, nums1_mid_idx: {nums1_mid_idx}, nums1_high_idx: {nums1_high_idx}')
            print(f'nums2_low_idx: {nums2_low_idx}, nums2_mid_idx: {nums2_mid_idx}, nums2_high_idx: {nums2_high_idx}')
            
            print(f'nums1_mid_val: {nums1_mid_val}')
            print(f'nums2_mid_val: {nums2_mid_val}')

            if nums1_mid_val <= nums2_mid_val:
                print('nums1_mid_val <= nums2_mid_val')
                nums_lower2 = nums1_mid_idx + nums2_mid_idx + 1
                print(f'nums_lower2: {nums_lower2}')
                nums1_higher = len(nums1) - nums1_mid_idx - 1
                nums2_higher = len(nums2) - nums2_mid_idx - 1
                nums_higher1 = nums1_higher + nums2_higher + 1
                print(f'nums_higher1: {nums_higher1}')

                if nums_lower2 == median_idx:
                    if nums1_mid_idx == len(nums1) - 1 or nums1[nums1_mid_idx + 1] >= nums2_mid_val:
                        return nums2_mid_val
                    else:
                        # raise nums2
                        nums2_low_idx = nums2_mid_idx + 1

                elif nums_higher1 == median_idx:
                    if nums2_mid_idx == len(nums2) - 1 or nums2[nums2_mid_idx + 1] >= nums1_mid_val:
                        return nums1_mid_val
                    else:
                        # lower nums1
                        nums1_high_idx = nums1_mid_idx - 1


                # Too low, raise nums1
                elif nums_higher1 > median_idx:
                    print('raise nums1')
                    nums1_low_idx = nums1_mid_idx + 1
                # Too high, lower nums2
                elif nums_lower2 > median_idx:
                    nums2_high_idx = nums2_mid_idx - 1
                    print('lower nums2')
                # Too high and too low
                else:
                    print('lower and raise')
                    nums2_high_idx = nums2_mid_idx
                    nums1_low_idx = nums1_mid_idx

            # Invert logic
            elif nums1_mid_val > nums2_mid_val:
                print('nums1_mid_val > nums2_mid_val')
                nums_lower1 = nums1_mid_idx + nums2_mid_idx + 1
                print(f'nums_lower1: {nums_lower1}')
                nums1_higher = len(nums1) - nums1_mid_idx - 1
                nums2_higher = len(nums2) - nums2_mid_idx - 1
                nums_higher2 = nums1_higher + nums2_higher + 1
                print(f'nums_higher2: {nums_higher2}')

                if nums_lower1 == median_idx:
                    if nums2_mid_idx == len(nums2) - 1 or nums2[nums2_mid_idx + 1] >= nums1_mid_val:
                        return nums1_mid_val
                    else:
                        # raise nums1
                        nums1_low_idx = nums1_mid_idx + 1

                elif nums_higher2 == median_idx:
                    if nums1_mid_idx == len(nums1) - 1 or nums1[nums1_mid_idx + 1] >= nums2_mid_val:
                        return nums2_mid_val
                    else:
                        # lower nums2
                        nums2_high_idx = nums2_mid_idx - 1


                # Too low, raise nums2
                if nums_higher2 > median_idx:
                    print('raise nums2')
                    nums2_low_idx = nums2_mid_idx + 1
                # Too high, lower nums1
                elif nums_lower1 > median_idx:
                    nums1_high_idx = nums1_mid_idx - 1
                    print('lower nums1')
                # Too high and too low
                else:
                    print('lower and raise')
                    nums1_high_idx = nums1_mid_idx
                    nums2_low_idx = nums2_mid_idx
