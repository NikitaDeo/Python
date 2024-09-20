class Solution:
    def time_to_minutes(self, time):
        """Convert 'HH:MM' time format to total minutes since midnight."""
        hours, minutes = map(int, time.split(':'))
        return hours * 60 + minutes

    def findMinDifference(self, timePoints):
        minutes_list = [self.time_to_minutes(time) for time in timePoints]
        minutes_list.sort()
        min_diff = float('inf')
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])
        circular_diff = (1440 + minutes_list[0] - minutes_list[-1]) % 1440
        min_diff = min(min_diff, circular_diff)
        return min_diff
timePoints1 = ["23:59", "00:00"]
timePoints2 = ["00:00", "23:59", "00:00"]

solution = Solution()
print(solution.findMinDifference(timePoints1))
print(solution.findMinDifference(timePoints2))