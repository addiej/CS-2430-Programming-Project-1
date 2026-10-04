def quicksort(numbers):

    if len(numbers) <= 1:
        return numbers

    pivot = numbers[len(numbers) // 2]

    smaller = []
    equal = []
    greater = []

    for number in numbers:
        if number < pivot:
            smaller.append(number)
        elif number == pivot:
            equal.append(number)
        else:
            greater.append(number)

    sorted_smaller = quicksort(smaller)
    sorted_greater = quicksort(greater)

    return sorted_smaller + equal + sorted_greater