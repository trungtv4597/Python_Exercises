def my_find(haystack, needle):
    """
    Find and return the index of needle in haystack.
    Return -1 if needle does not occur in haystack.
    """
    for index, letter in enumerate(haystack):
        if letter == needle:
            return index
    return -1

haystack = "Bananarama!"
print(haystack.find('a'))
print(my_find(haystack,'a'))