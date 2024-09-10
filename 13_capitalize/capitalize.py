def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    #  capitalize the first letter of a phrase
    if not phrase:
        return phrase
    return phrase[0].upper() + phrase[1:]

capitalize('python')
