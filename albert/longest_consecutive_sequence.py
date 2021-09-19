class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = set()
        begin_end = {}
        end_begin = {}
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            # new sequence
            if num - 1 not in end_begin and num + 1 not in begin_end:
                begin_end[num] = num
                end_begin[num] = num

            
            elif num + 1 in begin_end and num - 1 in end_begin:
                merge_begin = end_begin[num - 1]
                merge_end = begin_end[num + 1]
                begin_end[merge_begin] = merge_end
                end_begin[merge_end] = merge_begin
                del begin_end[num + 1]
                del end_begin[num - 1]

            # merge by extending end
            elif num - 1 in end_begin:
                existing_begin = end_begin[num - 1]
                end_begin[num] = existing_begin
                del end_begin[num - 1]

                begin_end[existing_begin] = num

            # merge by extending beginning
            elif num + 1 in begin_end:
                existing_end = begin_end[num + 1]
                begin_end[num] = existing_end
                del begin_end[num + 1]

                end_begin[existing_end] = num
            
            
        print(begin_end)

        return max([end - begin + 1 for begin, end in begin_end.items()])
