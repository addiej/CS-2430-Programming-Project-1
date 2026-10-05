'''Code author: Addie Hurst'''
# Heapsort.py

numbers = [1, 2, 3]

def heapsort(numbers):
    # Initialize the comparison counter and determine the size of the heap.
    comparisons = 0
    heapSize = len(numbers)

    # Start with the last parent that can have children in the heap.
    parentIndex = (heapSize // 2) - 1

    # Build a max heap by working backward through each parent.
    while parentIndex >= 0:
        currentParent = parentIndex

        # Continue moving down this section of the heap until the
        # parent is larger than its children.
        while True:
            # Find the indexes of the current parent's left and right children.
            leftChild = 2 * currentParent + 1
            rightChild = leftChild + 1
            largest = currentParent
            
            # If the left child exists, compare it with the largest value
            # found so far. Count only the element-to-element comparison.
            if leftChild < heapSize:
                comparisons = comparisons + 1
                if numbers[leftChild] > numbers[largest]:
                    largest = leftChild
                    
            # If the right child exists, compare it with the largest value
            # found so far. Count only the element-to-element comparison.
            if rightChild < heapSize:
                comparisons = comparisons + 1
                if numbers[rightChild] > numbers[largest]:
                    largest = rightChild

            # If the parent is already the largest value, this section
            # of the heap does not need another swap.
            if largest == currentParent:
                break

            # Swap the parent with the larger child.
            temporaryValue = numbers[currentParent]
            numbers[currentParent] = numbers[largest]
            numbers[largest] = temporaryValue

            # Continue checking downward from the position where the
            # parent value was moved.
            currentParent = largest

        # Move backward to the previous parent in the heap.
        parentIndex = parentIndex - 1

    # Repeatedly move the largest remaining value to the end of the
    # unsorted portion of the list.
    while heapSize > 1:
        lastUnsortedIndex = heapSize - 1

        # Swap the largest value at the beginning of the heap with the
        # last value in the unsorted portion.
        temporaryValue = numbers[0]
        numbers[0] = numbers[lastUnsortedIndex]
        numbers[lastUnsortedIndex] = temporaryValue

        # The value moved to the end is now sorted, so reduce the size
        # of the remaining unsorted heap.
        heapSize = heapSize - 1

        # Begin reorganizing the remaining heap from its first parent.
        currentParent = 0

        while True:
            # Find the indexes of the current parent's children.
            leftChild = 2 * currentParent + 1
            rightChild = leftChild + 1
            largest = currentParent

            # Compare an existing left child with the largest value
            # found so far and record the element comparison.
            if leftChild < heapSize:
                comparisons = comparisons + 1
                if numbers[leftChild] > numbers[largest]:
                    largest = leftChild
                    
            # Compare an existing right child with the largest value
            # found so far and record the element comparison.
            if rightChild < heapSize:
                comparisons = comparisons + 1
                if numbers[rightChild] > numbers[largest]:
                    largest = rightChild

            # Stop moving downward when the parent is already larger
            # than both of its existing children.
            if largest == currentParent:
                break

            # Swap the parent with its larger child.
            temporaryValue = numbers[currentParent]
            numbers[currentParent] = numbers[largest]
            numbers[largest] = temporaryValue

            # Continue checking from the new position of the moved value.
            currentParent = largest

    # Display the total element-to-element comparisons and return
    # the completed sorted list.
    print (f"Number of comparisons: {comparisons}")
    return numbers

print(f"Heap-sorted array: {heapsort(numbers)}")
