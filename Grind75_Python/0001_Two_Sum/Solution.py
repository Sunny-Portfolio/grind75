from typing import List


class Solution:
    # Solution 1: Brute Force
    # Time Complexity: O(n^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return []


    # Solution 2.1
    # 2 pass with hashmap
    def twoSum2(self, nums: List[int], target:int) -> List[int]:
        hashmap = {}    # same as dictionary

        # fill in the hashmap
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        # find in hashmap
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


    # Solution 2.2
    # Alternative 1 pass without hashmap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums and i != nums.index(complement):
                return [i, nums.index(target - nums[i])]

        return []

    # Solution 3
    # 1 pass with hashmap
    # Iterate and add to hashmap while also check if complement is in hashmap
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # same as dictionary
        # find in hashmap
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i


print(Solution().twoSum([3,2,3],6))