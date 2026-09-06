class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        counter = 0

        for i in nums:
            if i == 1:
                counter += 1
                if counter > max:
                    max = counter
            if i == 0:
                counter = 0

        return max