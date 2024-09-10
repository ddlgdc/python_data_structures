def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    bal = 0

    for each in parens:
        if each == '(':
            bal += 1
        elif each == ')':
            bal -= 1
        if bal < 0:
            return False
    return bal == 0

valid_parentheses("()")