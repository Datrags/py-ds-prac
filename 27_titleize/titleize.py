def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    s = ""

    for i in range(0, len(phrase)):
        if i == 0:
            s += phrase[i].upper()
        elif phrase[i - 1] != " ":
            s += phrase[i].lower()
        else:
            s += phrase[i].upper()
    
    return s

print(titleize('oNLy cAPITALIZe fIRSt'))