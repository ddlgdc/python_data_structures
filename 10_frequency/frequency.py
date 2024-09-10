def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    # returning the frequency of the desired value

    counter = 0

    for each in lst:
        if each == search_term:
            counter += 1
    return counter
    
print(frequency([1, 4, 3, 4, 4], 4))
print(frequency([1, 4, 3], 7))