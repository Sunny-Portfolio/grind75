from typing import List


class Solution:

    # Basic solution: Linear search
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        print('intervals %s newInterval %s' % (intervals, newInterval))
        pos = 0
        tempList = []

        # No overlapping: old interval < start of newInterval
        while pos < len(intervals) and intervals[pos][1] < newInterval[0]:
            tempList.append(intervals[pos])
            pos += 1

        # Overlapping: Need to find the range of the overlapping interval
        while pos < len(intervals) and intervals[pos][0] <= newInterval[1]:
            print('newInterval %s intervals %s ' % (newInterval, intervals[pos]))
            newInterval[0] = min(newInterval[0], intervals[pos][0])
            newInterval[1] = max(newInterval[1], intervals[pos][1])
            pos += 1
        tempList.append(newInterval)

        # Add the rest of the interval
        while pos < len(intervals):
            tempList.append(intervals[pos])
            pos += 1

        return tempList




# Test case
sol = Solution()
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

# intervals = [[1,3],[6,9]]
# newInterval = [2,5]

result = sol.insert(intervals, newInterval)

print('result %s' % (result))