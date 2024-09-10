def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """

    result = 1
    has_even = False

    for each in nums:
        if each % 2 == 0:
            result *= each 
            has_even = True
    if not has_even:
        return 1
    
    return result

print(multiply_even_numbers([2, 3, 4, 5, 6]))  
print(multiply_even_numbers([3, 4, 5]))        
print(multiply_even_numbers([1, 3, 5]))  