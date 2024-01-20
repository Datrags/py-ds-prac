def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    new_str = ""
    for i in range(len(phrase) - 1, -1, -1):
        print(i)
        new_str += phrase[i]
    return new_str
\
