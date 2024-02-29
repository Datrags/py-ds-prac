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
    c1 = 0
    c2 = 0

    for p in parens:
        if p == "(":
            c1 += 1
        elif p == ")":
            if c1 == 0:
                return False
            c2 += 1
    return c1 == c2

print(valid_parentheses("()"))
#True

print(valid_parentheses("()()"))
#True

print(valid_parentheses("(()())"))
#True

print(valid_parentheses(")()"))
#False

print(valid_parentheses("())"))
#False

print(valid_parentheses("((())"))
#False

print(valid_parentheses(")()("))