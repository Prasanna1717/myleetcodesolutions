class Solution(object):
    def twoSum(self, nums, target):
        prevhm = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevhm:
                return [prevhm[diff], i]
            prevhm[n] = i
        return

        
