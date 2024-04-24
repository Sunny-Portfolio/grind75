from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        tryNum = nums[0]
        i = 0
        j = 0
        k = 0
        tempList = []

        while i < len(nums):
            while j < len(nums):
                tryNum = nums[i] + nums[j]
                print('----------------')
                print('i %s j %s tryNum %s' % (i, j, tryNum))

                if tryNum * -1 in nums and i != j and j != k and k != i:
                    k = nums.index(tryNum * -1)
                    list = [nums[i], nums[j], nums[k]]
                    print('---- i %s j %s k %s List %s' % (i, j, k, list))
                    print('sorted list is %s tempList %s' % (sorted(list), sorted(tempList)))

                    print('is it in? ', any(tuple(sorted(set1)) == tuple(sorted(list)) for set1 in tempList))
                    # if not any(tuple(sorted(set1)) == tuple(sorted(list)) for set1 in tempList):
                    if not any(sorted(set1) == sorted(list) for set1 in tempList):
                        if (i != j and j != k and k != i):
                            print ('add')
                            tempList.append([nums[i], nums[j], nums[k]])

                    #tempList.append([nums[i], nums[j], nums[k]])

                j += 1
            i += 1
            j = 0

        return tempList


# nums = [-1, 0, 1, 2, -1, -4]
# nums = [1,2,-2,-1]
nums = [0,0,0]

sol = Solution()
print(sol.threeSum(nums))
