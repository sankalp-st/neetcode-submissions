class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        list1 = [[freq, num] for num, freq in hashmap.items()]
        list1.sort(reverse=True)

        return [list1[i][1] for i in range(k)]
