class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index, i in enumerate(nums):
            if target-i in hashmap:
                return [hashmap[target-i], index]
            
            else:
                hashmap[i] = index
