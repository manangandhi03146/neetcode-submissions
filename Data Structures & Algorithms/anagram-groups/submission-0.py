class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = {}
        for string in strs:
            counts = [0] * 26
            for char in string:
                idx = ord(char)-ord('a')
                counts[idx] += 1
            
            key = tuple(counts)

            if key in hash_map:
                hash_map[key].append(string)
            else:
                hash_map[key] = [string]
        
        return list (hash_map.values())