'''The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.'''

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        candidate=0
        for num in nums:
            if c==0:
                candidate=num
                c+=1
            elif candidate==num:
                c+=1
            else:
                c-=1
        return candidate
