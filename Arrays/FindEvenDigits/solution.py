class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        numeven = 0 
        for num in nums:
            if len(str(num)) % 2 == 0:
                numeven=numeven+1
        return(numeven)
                
        
        