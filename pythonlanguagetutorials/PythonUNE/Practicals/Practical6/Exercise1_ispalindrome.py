

def isPalindrome(word):
    if len(word) == 1 or len(word) == 0:
        return True
    if word[0] != word[-1]:
        return False

    return isPalindrome(word[1:-1])


assert isPalindrome("racecar")
assert not isPalindrome("banana")
assert isPalindrome("docnoteidissentafastneverpreventsafatnessidietoncod")
