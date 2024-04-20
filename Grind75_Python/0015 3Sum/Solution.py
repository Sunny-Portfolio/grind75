from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        tryNum = nums[0]
        i = j = 0
        k = -1
        tempList = []

        while i < len(nums):
            while j < len(nums):
                tryNum = nums[i] + nums[j]
                print('i %s j %s tryNum %s' % (i, j, tryNum))

                if tryNum * -1 in nums and i != j != k:
                    k = nums.index(tryNum * -1)
                    list = [nums[i], nums[j], nums[k]]
                    print('sorted list is %s tempList %s' % (sorted(list), sorted(tempList)))

                    print('is it in? ', any(tuple(sorted(set1)) == tuple(sorted(list)) for set1 in tempList))
                    # if not any(tuple(sorted(set1)) == tuple(sorted(list)) for set1 in tempList):
                    if not any(sorted(set1) == sorted(list) for set1 in tempList):

                        tempList.append([nums[i], nums[j], nums[k]])

                    #tempList.append([nums[i], nums[j], nums[k]])

                j += 1
            i += 1

        return tempList


nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
print(sol.threeSum(nums))
