#Team 3
#Team members Addie Hurst, Erich Mundt
#CS 2430 - 502
#Programming Project 1 – Fall 2026
#Primary Author: Erich M.

'''Author: Erich M.'''
def mergeSort(numbers):
    if len(numbers) == 1:
        return numbers[:], 0

    middle = len(numbers) // 2
    left, leftCount = mergeSort(numbers[:middle])
    right, rightCount = mergeSort(numbers[middle:])

    merged, mergeCount = merge(left, right)

    return merged, leftCount + rightCount + mergeCount

def merge(left, right):
    merged = []
    i = 0
    j = 0
    comparisons = 0

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(right[j:])
    merged.extend(left[i:])

    return merged, comparisons
