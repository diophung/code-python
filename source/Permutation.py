r# Problem: given a string, find all permutation of this string
# (i.e : repeated character is not countered)
# permute("abc") -> abc, acb, bac, bca, cab, cba


def Permute(s):
    output = []
    if len(s) == 1:
        return [s]

    first_char = s[:1]
    remaining_chars = s[1:]
    permutations = Permute(remaining_chars)
    print(first_char)
    print(remaining_chars)
    print(permutations)
    for p in permutations:
        output.append(first_char + p)

    return output


str = "abc"
perms = Permute(str)
print(perms)
