
"""
Anagram using lists
"""
def is_anagram_lists( s: str, t: str) -> bool:

    my_list = [0] * 26

    for c in s:
        if c in t :
            my_list[int(c)] = my_list[int(c)]+1
        else:
            return False
            # t contains c - add c

     # t does not contain c return false
    for c in t:
        my_list[int(c)] = my_list[int(c)] - 1

    for i in my_list:
        if i != 0:
            return False

        # check length of r and t to be same
    return True  # len(r) == len(t)

"""
Anagram using dictionaries
"""
def is_anagram_dictionary( s: str, t: str) -> bool:

        # create a dict t
    r = dict()
    for c in s:
        if c in t :
            if c in r :
                i = r[c]
                r[c] = i + 1
            else:
                r[c] = 1
        else:
            return False
            # t contains c - add c

     # t does not contain c return false
    for c in t:
        if c in r :
            i = r[c]
            r[c] = i - 1
        else:
            return False

    for (k, v) in r.items():
        if v > 0:
            return False

        # check length of r and t to be same
    return True  # len(r) == len(t)

#print(is_anagram_lists("racecar","carrace"))
#print(is_anagram_lists("racecar","caarace"))


print(is_anagram_dictionary("racecar","carrace"))
print(is_anagram_dictionary("racecar","caarace"))