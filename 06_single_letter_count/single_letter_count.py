def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """
    letter_counter = 0
    lower_case_word = word.lower()
    lower_case_letter = letter.lower()

    for each in lower_case_word:
        if each == lower_case_letter:
            letter_counter += 1
    return(letter_counter)

single_letter_count('Hello World', 'l')