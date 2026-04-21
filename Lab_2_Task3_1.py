def smallest(n:float, m:float) -> float:
    if n < m:
        return n #For which calls below is this statement evaluated?
        # neither
    else:
        return m

first = smallest(3,2) #What is the value of first?
# The value of first is 2.
second = smallest(2,2) #What is the value of second? Is this a reasonable result? Why or why not?
# The value of second is 2. # This is reasonable because n is not less than m, so the function returns m which is 2.
print()
