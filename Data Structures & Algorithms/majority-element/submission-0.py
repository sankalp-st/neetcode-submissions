class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        h_nums = {}
        for i in nums:
            if i in h_nums:
                h_nums[i]+=1
            else:
                h_nums[i] = 1

        for k,v in h_nums.items():
            if v>(size/2):
                return k

        