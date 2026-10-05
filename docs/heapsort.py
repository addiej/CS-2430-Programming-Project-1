'''Code author: Addie Hurst'''
#Heapsort.py
numbers = []

def heapsort(numbers, heapSize, parentIndex):
    leftChild = 2 * parentIndex + 1

    #determine which is largest:
        #parent
        #left child
        #right child
    #if a child is larger than the parent:
        #swap them
        #'heap-ify' the affected section again

#The largest number is now at the beginning
#Swap:
    #(first element) with (last unsorted element)
#then, consider the last element sorted
#Reduce the size of the unsorted heap
#'Heapify' the remaining unsorted portion again
#Repeat until sorted
#Return the sorted array

heapsort(numbers)
