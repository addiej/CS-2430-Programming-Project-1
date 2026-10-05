#Heapsort.py
'''Code author: Addie Hurst'''

numbers = [4, 10, 3, 5, 1]
heapSize = len(numbers)
parentIndex = 0

def heapsort(numbers, heapSize, parentIndex):
    leftChild = 2 * parentIndex + 1
    rightChild = leftChild + 1
    largest = parentIndex
    #compare left child against numbers[largest]
    if leftChild > x :
        largest = leftChild

    #compare right child against numbers[largest]
    if rightChild > y:
        largest = rightChild
#The largest number is now at the beginning
#Swap:
    #(first element) with (last unsorted element)
#then, consider the last element sorted
#Reduce the size of the unsorted heap
#'Heapify' the remaining unsorted portion again
#Repeat until sorted
#Return the sorted array

heapsort(numbers, heapSize, parentIndex)
