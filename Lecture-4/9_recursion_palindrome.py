# def palindrome(*args):
#     word = args[0]
#     if word == word[::-1]:
#         return f'{word} is a palindrome'
#     else:
#         return f"{word} is not a palindrome"


def palindrome(word, index_) -> str:
    def recursive(word, index_):
        if len(word) == index_:
            return ''
        if len(word) > 0:
            retval = word[-1] + str(recursive(word[:-1], index_))
        return retval

    retval = recursive(word, index_)
    if retval == word:
        return f'{word} is a palindrome'
    else: 
        return f'{word} is not a palindrome'

print(palindrome("abcba", 0))
print(palindrome("peter", 0))
