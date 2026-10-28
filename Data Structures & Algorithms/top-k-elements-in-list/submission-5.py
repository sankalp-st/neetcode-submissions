class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ans = []
        ans2 = []
        for i in nums:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] = 1
        for i,v in hashmap.items():
            ans.append([v,i])
        ans.sort(reverse = True)
        for i in range(k):
            ans2.append(ans[i][1])
        return ans2

        