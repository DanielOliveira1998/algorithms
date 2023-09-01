def find_duplicate(nums):
    """Faça o código aqui."""
    frequency = {}
    if len(nums) == 1 or len(nums) == 0:
        return False
    for num in nums:
        if isinstance(num, str) or num < 0:
            return False
        if num in frequency:
            return num
        else:
            frequency[num] = 1
    return False
