class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        contains = set(nums)

        max_len = 0
        for n in nums:
            if n - 1 in contains:
                continue
            curr, curr_len = n, 0
            while curr in contains:
                curr += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
        
        return max_len