'''Code author: Addie Hurst'''
# Heapsort.py

numbers = [1, 2, 3]

def heapsort(numbers):
    comparisons = 0
    heapSize = len(numbers)
    parentIndex = (heapSize // 2) - 1

    while parentIndex >= 0:
        currentParent = parentIndex
        while True:
            leftChild = 2 * currentParent + 1
            rightChild = leftChild + 1
            largest = currentParent
            
            if leftChild < heapSize:
                comparisons = comparisons + 1
                if numbers[leftChild] > numbers[largest]:
                    largest = leftChild
                    
            if rightChild < heapSize:
                comparisons = comparisons + 1
                if numbers[rightChild] > numbers[largest]:
                    largest = rightChild

            if largest == currentParent:
                break

            temporaryValue = numbers[currentParent]
            numbers[currentParent] = numbers[largest]
            numbers[largest] = temporaryValue

            currentParent = largest

        parentIndex = parentIndex - 1

    while heapSize > 1:
        lastUnsortedIndex = heapSize - 1

        temporaryValue = numbers[0]
        numbers[0] = numbers[lastUnsortedIndex]
        numbers[lastUnsortedIndex] = temporaryValue

        heapSize = heapSize - 1

        currentParent = 0

        while True:
            leftChild = 2 * currentParent + 1
            rightChild = leftChild + 1
            largest = currentParent

            if leftChild < heapSize:
                comparisons = comparisons + 1
                if numbers[leftChild] > numbers[largest]:
                    largest = leftChild
                    
            if rightChild < heapSize:
                comparisons = comparisons + 1
                if numbers[rightChild] > numbers[largest]:
                    largest = rightChild

            if largest == currentParent:
                break

            temporaryValue = numbers[currentParent]
            numbers[currentParent] = numbers[largest]
            numbers[largest] = temporaryValue

            currentParent = largest
    print (f"Number of comparisons: {comparisons}")
    return numbers

print(f"Heap-sorted array: {heapsort(numbers)}")
