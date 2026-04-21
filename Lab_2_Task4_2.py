def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])    # For which call below is this statement evaluated - First because it has length of list >2 for first
    elif len(L) > 1:                                  #   and what are the values being added?  9
        result = len(L[0]) + len(L[1])                # For which call below is this statement evaluated - third  because it has length of list>1 for third.
    elif len(L) > 0:                                  #   and what are the values being added? 11
        result = len(L[0])                            # For which call below is this statement evaluated - second because it has length of list>0 for second.
    else:                                             # and what are the values being added? 11
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()