def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter = {}

    for each in nums:
        if each in counter:
            counter[each] += 1
        else:
            counter[each] = 1
    
    highest = max(counter, key=counter.get)
    return highest

mode([2, 2, 3, 3, 2])