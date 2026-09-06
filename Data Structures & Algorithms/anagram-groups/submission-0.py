class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list1 = {}

        for i in strs:
            key = "".join(sorted(i))
            if key in list1:
                list1[key].append(i)
            else:
                list1[key] = [i]
        return list(list1.values())
        