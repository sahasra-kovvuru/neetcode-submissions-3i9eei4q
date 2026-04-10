class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            count = 0
            for j in nums:
                if i == j:
                    count += 1
            counts.update({i:count})
        values = list(counts.values())
        values.sort(reverse=True)

        output = []
        used = set()
        for i in range(k):
            for key,v in counts.items():
                if v == values[i] and key not in used:
                    output.append(key)
                    used.add(key)
                    if len(output) == k:
                        return output 
            
                

        