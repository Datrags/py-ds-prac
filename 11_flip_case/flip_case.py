def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    s = ""
    for i in phrase:
        if i.lower() == to_swap.lower():
            if i.islower():
                s += i.upper()
            else:
                s += i.lower()
        else:
            s += i
    return s

