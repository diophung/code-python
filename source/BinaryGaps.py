# Problem :
"""
A binary gap within a positive integer N is any maximal sequence of
consecutive zeros that is surrounded by ones at both ends in the binary
representation of N. For example, number 9 has binary representation 1001
and contains a binary gap of length 2. The number 529 has binary
representation 1000010001 and contains two binary gaps: one of length 4
and one of length 3. The number 20 has binary representation 10100 and
contains one binary gap of length 1. The number 15 has binary
representation 1111 and has no binary gaps.
Write a function:

    def solution(N)

that, given a positive integer N, returns the length of its longest
binary gap. The function should return 0 if N doesn't contain a binary gap.
For example, given N = 1041 the function should return 5, because N has
binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that: N is an integer within the range [1..2,147,483,647].

Complexity:
expected worst-case time complexity is O(log(N)).
expected worst-case space complexity is O(1).
"""


class BinaryGaps:
    @staticmethod
    def solution(N):
        if N < 0:
            return -1
        if N <= 1:
            return 0
        binary_format = bin(N)[2:]
        max_len = 0
        seq_started = False
        temp_len = 0
        for char in binary_format:
            if char == "1":
                # starting seq
                if seq_started is False:
                    seq_started = True
                    temp_len = 0
                # ending seq
                if seq_started is True:
                    if temp_len > max_len:
                        max_len = temp_len
                    temp_len = 0
            if char == "0":
                if seq_started:
                    temp_len += 1

        return max_len


bin_gap = BinaryGaps()
print(bin_gap.solution(1041))  # expect 5
print(bin_gap.solution(0))  # expect 0
print(bin_gap.solution(1))  # expect 0
print(bin_gap.solution(10))  # expect 1 1010
