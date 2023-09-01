def is_palindrome_iterative(word):
    """Faça o código aqui."""
    if len(word) == 0:
        return False
    low_index = 0
    high_index = len(word) - 1
    # for i, char in word:
    #     if i < high_index:
    #         if char != word[high_index]:
    #             return False
    #         else:
    #             high_index -= 1
    #     return True
    while low_index < high_index:
        if word[low_index] != word[high_index]:
            return False
        low_index += 1
        high_index -= 1
    return True
