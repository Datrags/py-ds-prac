def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    VOWELS = ['a', 'e', 'i', 'o', 'u']
    s_vowels = []
    # Reverse vowel order
    s_vowels = s_vowels[::-1]
    for i in range(len(s)):
        if s[i].lower() in VOWELS:
            s_vowels.append(s[i])
    
    new_str = ""
    for i in range(len(s)):
        if s[i].lower() in VOWELS:
            new_str += s_vowels.pop()
        else:
            new_str += s[i]

    print(new_str)
    return new_str

