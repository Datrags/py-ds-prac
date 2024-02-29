def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    VOWELS = ["a","e","i",'o','u']
    d = {}

    for letter in phrase:
        if letter.lower() in VOWELS:
            l = letter.lower()
            if l in d:
                d[l] += 1
            else:
                d[l] = 1
    

    return d


print(vowel_count('HOW ARE YOU? i am great!'))