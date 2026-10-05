'''Code author: Addie Hurst'''
# Heapsort.py

numbers = [4, 10, 3, 5, 1]

def heapsort(numbers):
    heapSize = len(numbers)
    parentIndex = (heapSize // 2) - 1

    while parentIndex >= 0:
        currentParent = parentIndex
        while True:
            leftChild = 2 * currentParent + 1
            rightChild = leftChild + 1
            largest = currentParent

            if leftChild < heapSize:
                if numbers[leftChild] > numbers[largest]:
                    largest = leftChild

            if rightChild < heapSize:
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
                if numbers[leftChild] > numbers[largest]:
                    largest = leftChild

            if rightChild < heapSize:
                if numbers[rightChild] > numbers[largest]:
                    largest = rightChild

            if largest == currentParent:
                break

            temporaryValue = numbers[currentParent]
            numbers[currentParent] = numbers[largest]
            numbers[largest] = temporaryValue

            currentParent = largest

    return numbers
print("Heap-sorted array: ")
print(heapsort(numbers))
