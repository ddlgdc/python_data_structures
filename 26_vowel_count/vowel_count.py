def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_freq = {}
    lowercase_phrase = phrase.lower()

    for each in lowercase_phrase:
        if each in vowels: 
            if each in vowel_freq:
                vowel_freq[each] += 1
            else:
                vowel_freq[each] = 1
    return vowel_freq

vowel_count('HOW ARE YOU? i am great!')