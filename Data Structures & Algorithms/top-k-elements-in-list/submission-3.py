class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count frequencies
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Sort by frequency descending
        sorted_items = sorted(
            count.items(),
            key=lambda x: x[1],
            reverse=True
        )

        ans = []

        for i in range(k):
            ans.append(sorted_items[i][0])

        return ans