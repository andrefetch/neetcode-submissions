class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0] * len(nums)
        
        product = math.prod(nums)
        product_without_zero = 1

        for n in nums:
            if n == 0:
                continue
            product_without_zero *= n
        
        res = []
        for n in nums:
            if n == 0:
                res.append(product_without_zero)
            else:
                res.append(int(product/n))

        return res