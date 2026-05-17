class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            digits = list(str(num))
            for digiting in digits:
               result.append(int(digiting))  
        return result
    
