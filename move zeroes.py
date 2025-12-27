'''Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        idx=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[idx]=nums[i]
                idx+=1
        for i in range(idx,len(nums)):
            nums[i]=0
