class Solution:
    def majorityElement(self, nums: List[int]) -> int:
            cand, cnt = None, 0
            for n in nums:
                cnt == 0 and (cand := n)
                cnt += (1 if n == cand else -1)
                return cand

        