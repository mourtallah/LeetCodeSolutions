class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones=0
        maxones=0
        for i in nums:
            if i==1:
                ones = ones + 1
            else:
                if ones > maxones:
                    maxones=ones
                ones=0
            if ones > maxones:
                maxones=ones
        return(maxones)
        