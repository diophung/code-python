"""
problem: a frog can jump 1,2,3...n steps at a time. How many way it can jump exactly N-step
count_jump(1) = (1) = 1
count_jump(2) = (1,1), (2) = 2
count_jump(3) = (1,1,1), (1,2), (2,1), (3) = 4
count_jump(4) = (1,1,1,1), (1,1,2), (1,2,1), (1,3), (2,1,1), (2,2), (3,1), (4) = 8
"""

class FrogJump:
    def Solve(self, N):
