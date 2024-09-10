def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    #  flipping the case of the desired letter 

    res = ''

    for character in phrase:
        if character.lower() == to_swap.lower():
            if character.islower():
                res += character.upper()
            else: 
                res += character.lower()
        else:
            res += character
    return res

print(flip_case('Aaaahhh', 'a'))  # Output: 'aAAAhhh'
print(flip_case('Aaaahhh', 'A'))  # Output: 'aAAAhhh'
print(flip_case('Aaaahhh', 'h'))  # Output: 'AaaaHHH'