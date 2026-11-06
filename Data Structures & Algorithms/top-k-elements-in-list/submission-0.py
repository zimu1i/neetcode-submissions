class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedlist = sorted(nums)
        freq = {}
        output = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else: 
                freq[num] += 1
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        for j in range(k):
            output.append(sorted_freq[j][0])
        return output

        