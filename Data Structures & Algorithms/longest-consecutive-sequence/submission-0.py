class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1 =  set(nums)
        longest = 0
        for i in nums1:
            if i-1 not in nums1:
                current = i
                streak = 1
                while current+1 in nums1:
                    current+=1
                    streak+=1
                longest = max(longest, streak)
        return longest

                
        
        