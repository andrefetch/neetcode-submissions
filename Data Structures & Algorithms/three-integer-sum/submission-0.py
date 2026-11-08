class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen, used = set(), set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k = nums[i] + nums[j]
                k2 = abs(k) if k < 0 else -k
                hash = str(sorted([nums[i], nums[j], k2]))
                if k2 in seen and hash not in used:
                    res.append([nums[i], nums[j], k2])
                    used.add(hash)
            seen.add(nums[i])
        return res