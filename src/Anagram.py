# Problem: determine if 2 strings are anagrams
# Solution 1 : O(nlogn) : compared sorted strings.


def is_anagram_with_sorting(str_a, str_b):
    """
    check if 2 strings are anagrams
    @str_a : the first string
    @str_b : the second string
    """
    if str_a is None \
       or str_b is None:
            return False
    sorted_a = sorted(str_a)
    sorted_b = sorted(str_b)
    return sorted_a == sorted_b


print(is_anagram_with_sorting("tod", "dot"))  # expect True
print(is_anagram_with_sorting("bat", "bacteria"))  # expect False
print(is_anagram_with_sorting(None, "N"))  # expect False


def dict_from_string(str):
    """
    convert a string into dictionary of characters
    """
    # assum Latin-charset
    dict = [None] * 26
    for i in str:
        if dict[ord(i) - 97] is None:  # ord('a') = 97
            dict[ord(i) - 97] = 1
        else:
            dict[ord(i) - 97] += 1
    return dict


# Solution 2: compare count of characters, assume only Latin char (26-char)
def is_anagram_without_sorting(str_a, str_b):
    if str_a is None \
        or str_b is None \
            or len(str_a) != len(str_b):
        return False
    dictA = dict_from_string(str_a)
    dictB = dict_from_string(str_b)
    for index in range(len(dictA)):
        if dictA[index] != dictB[index]:
            return False
    return True


print(is_anagram_without_sorting("bat", "tab"))  # expect True
print(is_anagram_without_sorting("bac", "bacteria"))  # expect False
print(is_anagram_without_sorting(None, "N"))  # expect False
