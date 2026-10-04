'''TODO author: Addie Hurst'''
# TODO:
# - Add a comparison counter.
# - Count each left[i] <= right[j] comparison.
# - Do not count loop conditions or index comparisons.
# - Make the comparison count available to main.py.


'''Author: Erich M.'''
def mergeSort(numbers):
    if len(numbers) == 1:
        return numbers

    middle = len(numbers) // 2
    left = mergeSort(numbers[:middle])
    right = mergeSort(numbers[middle:])

    return merge(left, right)

def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(right[j:])
    merged.extend(left[i:])

    return merged
