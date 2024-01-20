def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    def multi_num(phrase):
        freq = {}

        for letter in phrase:
            if letter not in freq:
                freq[letter] = 1
            else:
                freq[letter] += 1

        return freq
    
    
    m = multi_num(nums)

    largest = 0
    for key in m:
        print(key,":",m[key])
        if m[key] > largest:
            largest = key

    return largest

print(mode([2, 2, 3, 3, 2]))