def shakerSort(numbers):
    #work on copy, to keep original intact
    arr = numbers[:]
    comparisons = 0

    #Set swapped to true
    swapped = True
    #Set start to beginning of array
    start = 0
    #Set end to end of array
    end = len(arr) - 1

    #WHILE swapped is true
    while swapped:
        #Set swapped to false
        swapped = False

        #FOR each element form start to end (forward pass)
        for i in range(start, end):
            comparisons += 1
            #Compare current element with next element
            if arr[i] > arr[i + 1]:
                #Swap them
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        #IF no elements were swapped: stop
        if not swapped:
             break

        # Move end backward by one
        end -= 1

        #Set swapped to false
        swapped = False

        #FOR each element from end toward start (backward pass)
        for i in range(end - 1, start - 1, -1):
            comparisons += 1
            #Compare current element with next element
            if arr[i] > arr[i + 1]:
                #swap them
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # Move start forward by one
        start +=1
    return arr, comparisons