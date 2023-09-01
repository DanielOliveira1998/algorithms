def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    sorted_first = sorted(first_string.split(), key=str.lower)
    sorted_second = sorted(second_string.split(), key=str.lower)
    if len(first_string) == 0 or len(second_string) == 0:
        return False
    if (len(first_string) != len(second_string)):
        return (sorted_first, sorted_second, False)
    if (sorted_first == sorted_second):
        return (sorted_first, sorted_second, True)
