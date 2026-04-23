def inc(m:int) -> int:
    return m + 1                             # Record, in order of the calls, each value of m and
                                             # the corresponding return value.
                    #m = 3 -> 4; m = 4 -> 5


def check(n:int) -> bool:
    return n > 2                             # Record, in order of the calls, each value of n and
                                             # the corresponding return value.
                # n = 0 -> False; n = 1 -> False; n = 2 -> False; n = 3 -> True; n = 4 -> True

answer = [inc(x) for x in range(5) if check(x)]   # What is the value of answer? [4, 5]
print()