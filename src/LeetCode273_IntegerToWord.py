"""
Problem: Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""


class IntegerToWord:
    def Solve(self, number):
        """
        :type num: int
        :rtype: str
        """
        word = ""
        return word


sol = IntegerToWord()
print(sol.Solve(1))
print(sol.Solve(11))
print(sol.Solve(12))
print(sol.Solve(123))
print(sol.Solve(123456))
print(sol.Solve(1002))
