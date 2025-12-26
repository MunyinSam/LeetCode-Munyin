
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    if len(s) != len(t):
        return False

    _dict = {}

    for letter in s:
        if letter not in _dict:
            _dict[letter] = 1
        
        _dict[letter] += 1

    for letter in t:
        if letter not in _dict:
            return False

        _dict[letter] -= 1
        if _dict[letter] <= 0:
            return False
    
    return True

print(isAnagram("ratt", "cart"))
        
        