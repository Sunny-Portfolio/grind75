# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->
Find non overlapping and overlapping interval

Alternatively, can also use binary search for slightly better performance
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(n)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(1)

# Code
```py
class Solution:
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
```