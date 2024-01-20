def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    # for i in range(0, len(phrase)):
    #     if phrase[i].isalpha():
    #         phrase = phrase.replace(phrase[i], phrase[i].upper())
    #         break
    
    # return phrase

    phrase = phrase[0].upper() + phrase[1:len(phrase)]
    return phrase

print(capitalize("python"))
print(capitalize("only first word"))
