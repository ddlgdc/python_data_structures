def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    num1_str = str(num1)
    num2_str = str(num2)
    
    freq1 = {}
    freq2 = {}

    for digit in num1_str:
        if digit in freq1:
            freq1[digit] += 1
        else:
            freq1[digit] = 1
            
    for digit in num2_str:
        if digit in freq2:
            freq2[digit] += 1
        else:
            freq2[digit] = 1

    return freq1 == freq2


print(same_frequency(551122, 221515))  # Output: True
print(same_frequency(321142, 3212215))  # Output: False
print(same_frequency(1212, 2211))  # Output: True
