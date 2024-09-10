def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # convert to lowercase and remove spaces
    normal_phrase = ''.join(phrase.lower().split())

    # convert to a list
    phrase_list = list(normal_phrase)

    # check if list is the same forwards and backwards
    return phrase_list == phrase_list[::-1]

# Test cases
print(is_palindrome('tacocat'))    # True
print(is_palindrome('noon'))       # True
print(is_palindrome('robert'))     # False
print(is_palindrome('taco cat'))   # True
print(is_palindrome('Noon'))       # True
