class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        hash_map={}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            
            else:
                hash_map[num] = 1
        
        for num, freq in hash_map.items():
            buckets[freq].append(num)

        res=[]
        for freq in range(len(buckets) -1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        

            