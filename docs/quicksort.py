'''Author: Erich M.'''
def quicksort(numbers):

    if len(numbers) <= 1:
        return numbers[:], 0

    pivot = numbers[len(numbers) // 2]

    smaller = []
    equal = []
    greater = []
    comparisons = 0

    for number in numbers:
        comparisons += 1
        if number < pivot:
            smaller.append(number)
        elif number == pivot:
            equal.append(number)
        else:
            greater.append(number)

    sortedSmaller, smallerCount = quicksort(smaller)
    sortedGreater, greaterCount = quicksort(greater)

    result = sortedSmaller + equal + sortedGreater

    return result, comparisons + smallerCount + greaterCount