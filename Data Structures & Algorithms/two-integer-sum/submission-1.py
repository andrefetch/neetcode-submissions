class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
       hashmap = {}

       for i, n in enumerate(nums):

        needed_num = target - n
        if needed_num in hashmap:
            return [hashmap[needed_num], i]
        hashmap[n] = i
        
        
