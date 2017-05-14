# Problem 168 : Excel Sheet Column title and vice versa
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# For e.g:
#    1 -> A
#    2 -> B
#    3 -> C
#    ...
#    26 -> Z
#    27 -> AA
#    28 -> AB
#
# Then given a string [A-Z], convert it to the numerical column index
# For e.g:
# A -> 1
# AA -> 27
# AB -> 28
import math


class ExcelSheetColumn:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n > 0:
            n -= 1
            res = chr(n % 26 + 65) + res
            n = int(n / 26)
        return res

    def convertToNumber(self, title: str) -> int:
        num = 0
        length = len(title)
        power = length - 1
        if length == 1:
            return ord(title[0]) - ord('A') + 1
        for i in range(length):
            mult = ord(title[i]) - ord('A') + 1
            num += mult * math.pow(26, power)
            power -= 1
        return int(num)


sol = ExcelSheetColumn()
print('1->' + str(sol.convertToTitle(1)))  # 1 = 26*0 + 1 = A
print('26->' + str(sol.convertToTitle(26)))  # 26 = 26*0 + 26 = Z
print('27->' + str(sol.convertToTitle(27)))  # 27 = 26*1 + 1 = AA
print('52->' + str(sol.convertToTitle(52)))  # 52 = 26*1 + 26 = AZ
print('700->' + str(sol.convertToTitle(700)))  # 700 = 26*26 + 24 = ZX
print('703->' + str(sol.convertToTitle(703)))  # 703 = 1 * math.pow(26,2) + 1 * math.pow(26,2) + 1 = AAA
print('18278->' + str(sol.convertToTitle(18278)))  # 18278 = 26 * math.pow(26,2) + 26 * math.pow(26,1) + 26 * math.pow(26,0) = ZZZ
print('------------')
print('A->' + str(sol.convertToNumber('A')))  # 0*26 + 1 = 1
print('Z->' + str(sol.convertToNumber('Z')))  # 0*26 + 26 = 26
print('AA->' + str(sol.convertToNumber('AA')))  # 1*26 + 1 = 27
print('AZ->' + str(sol.convertToNumber('AZ')))  # AZ = 1*26 + 26 = 52
print('ZX->' + str(sol.convertToNumber('ZX')))  # ZX = 26*26 + 24 = 700
print('AAA->' + str(sol.convertToNumber('AAA')))  # 1 * math.pow(26,2) + 1 * math.pow(26,2) + 1 = 703
print('ZZZ->' + str(sol.convertToNumber('ZZZ'))) # ZZZ = 26 * math.pow(26,2) + 26 * math.pow(26,1) + 26= 18278
