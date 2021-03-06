"""
Given an array of m time intervals consisting
of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

For example,
[[0, 30],[5, 10],[15, 20]] ~ [[0,30], [5,20]] -> expect 2.

[[4, 9], [4, 17], [9, 10]] ~ [[4,10],[4,17]] -> expect 2

[[5, 8], [6, 8]] -> expect 2


Algo: sort by start time, and use PriorityQueue to keep track of
earliest ending m. Go from start to end: merge all
non-overlap m into one m. The length of the result
list is the number of m rooms needed

"""


class PriorityQueue:
    def __init__(self, items=[]):
        items = sorted(items, key=lambda item: item[0])
        self.items = items

    def Enqueue(self, item):
        # priority queue by ending time
        self.items.append(item)
        self.items = sorted(self.items, key=lambda m: m[1])

    def Dequeue(self):
        self.items = self.items[0]
        return self.items[0]

    def Peek(self):
        return self.items[0]


class MinMeetingRoom:
    def Solve(self, meetings: list) -> int:
        sorted_meetings = sorted(meetings, key=lambda i: i[0])
        queue = PriorityQueue()
        for m in sorted_meetings:
            if queue.items and m[0] >= queue.Peek()[1]:
                # non-overlapping -> merge
                queue.Peek()[1] = max(m[1], queue.Peek()[1])
            else:
                queue.Enqueue(m)
        return queue.items


sol = MinMeetingRoom()
# overlap
meetings = [[0, 30], [5, 10], [15, 20], [4, 30]]  # expect 3
print(sol.Solve(meetings))

# same end time
meetings = [[5, 8], [6, 8]]  # expect 2
print(sol.Solve(meetings))

# same start time
meetings = [[4, 9], [4, 17], [9, 10]]  # expect 2
print(sol.Solve(meetings))

# no overlap
meetings = [[1, 2], [3, 4], [8, 10]]  # expect 1
print(sol.Solve(meetings))
