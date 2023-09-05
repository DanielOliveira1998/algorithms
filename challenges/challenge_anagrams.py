def merge_sort(word, start=0, end=None):
    if end is None:
        end = len(word)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(word, start, mid)
        merge_sort(word, mid, end)
        merge(word, start, mid, end)
    return word


def merge(word, start, mid, end):
    left = word[start:mid]
    right = word[mid:end]
    left_index, right_index = 0, 0
    for general_index in range(start, end):
        if left_index >= len(left):
            word[general_index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            word[general_index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            word[general_index] = left[left_index]
            left_index += 1
        else:
            word[general_index] = right[right_index]
            right_index += 1


def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    lower_first = [char.lower() for char in first_string]
    lower_second = [char.lower() for char in second_string]
    sorted_first = "".join(merge_sort(lower_first))
    sorted_second = "".join(merge_sort(lower_second))
    if len(first_string) == 0 or len(second_string) == 0:
        return (sorted_first, sorted_second, False)
    elif (len(first_string) != len(second_string)):
        return (sorted_first, sorted_second, False)
    elif (sorted_first != sorted_second):
        return (sorted_first, sorted_second, False)
    else:
        return (sorted_first, sorted_second, True)
