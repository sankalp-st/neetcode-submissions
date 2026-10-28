class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        n = len(nums)

        prefix,postfix = 1,1

        for i in range(0,n):
            res[i] = prefix
            prefix*=nums[i]

        for i in range(n-1,-1,-1):
            res[i] *= postfix
            postfix *=nums[i]
        
        return res