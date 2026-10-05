'''Code author: Addie Hurst'''
#Heapsort.py
numbers = [4, 10, 3, 5, 1]
heapSize = len(numbers)
parentIndex = 0
def heapsort(numbers, heapSize, parentIndex):
    leftChild = 2 * parentIndex + 1
    rightChild = leftChild + 1
    largest = parentIndex
    if numbers[leftChild] > numbers[largest] :
        largest = leftChild
    if numbers[rightChild] > numbers[largest]:
        largest = rightChild
#The largest number is now at the beginning
#Swap:
    #(first element) with (last unsorted element)
#then, consider the last element sorted
#Reduce the size of the unsorted heap
#'Heapify' the remaining unsorted portion again
#Repeat until sorted
#Return the sorted array
    print("Largest index:", largest)
    print("Largest value:", numbers[largest])
heapsort(numbers, heapSize, parentIndex)
