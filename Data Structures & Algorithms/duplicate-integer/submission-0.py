class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = set()
        for i in range(0,len(nums)):
            nums1.add(nums[i])
        if len(nums)==len(nums1):
            return False
        else:
            return True
            
        