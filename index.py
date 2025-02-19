class Solution(object):
    nums = [2, 7, 11, 15]
    target = 9
    def twoSum(self, nums, target):
            map = {} 
            for i, num in enumerate(nums):
                if target - num in map:
                    return [i, map[target - num]]
                map[num] = i
