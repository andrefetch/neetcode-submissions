class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hm = collections.defaultdict(list)
        for s in strs:
            hash = str(sorted(list(s)))
            hm[hash].append(s)
        return list(hm.values())