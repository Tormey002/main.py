def is_anagram1(string1, string2):
    return sorted(string1) == sorted(string2)

print( is_anagram1("listen", "silent"))

def is_anagram2(str1, str2):
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    return (list1 == list2)

# print(is_anagram2("listen", "silent"))

from collections import Counter
def is_anagram3(string1, string2):
    c1 = Counter(string1)
    c2 = Counter(string2)
    return c1 == c2

# print(is_anagram3("listen", "silent"))
    