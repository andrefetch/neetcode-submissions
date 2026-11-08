class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = Counter(nums)

        countToVal = collections.defaultdict(list)

        for val, count in counter.items():
            countToVal[count].append(val)

        cnt = [-cnt for cnt in countToVal.keys()]
        heapq.heapify(cnt)
        
        res = []
        for i in range(len(cnt)):
            next_count = - heapq.heappop(cnt)
            for num in countToVal[next_count]:
                if len(res) == k:
                    return res
                res.append(num)    

        return res