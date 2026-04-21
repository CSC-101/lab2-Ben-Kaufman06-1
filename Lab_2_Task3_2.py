def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b # In general, when will a call to this function evaluate this statement?
    # A call to this function will evaluate this statement when a > b and a > c
    elif b > c:
        return b + c # In general, when will a call to this function evaluate this statement?
    # A call to this function will evaluate this statement when (b > c) and (a <=b or a<=c)
    else:
        return 2 * c #In general, when will a call to this function evaluate this statement?
    # A call to this function will evaluate this statement when (b <= c) and (a <=b or a<=c)

answer1 = function2(3, 2, 1) #What is the value of answer 1?
# The value of answer 1 is 1
answer2 = function2(2, 3, 1) #What is the value of answer 2?
# The value of answer 2 is 4
answer3 = function2(2, 1, 3) #What is the value of answer 3?
#the value of answer 3 is 6
print()