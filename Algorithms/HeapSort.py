# Heap Sort

import heapq
import random

def heap_sort(arr):
    
    # Turn the list into a valid heap
    heapq.heapify(arr)
    
    # Pop elements one by one to get them in sorted order
    sorted_list = [heapq.heappop(arr) for _ in range(len(arr))]
    
    return sorted_list

# Test Heap
if __name__ == "__main__":
    print("\n=== Heap Sort Test ===")

    # Generate 100 random integers between 1 and 1000
    random_numbers = [random.randint(1, 1000) for _ in range(100)]
    
    print("Unsorted List:", random_numbers)

    # Sort using heap sort
    sorted_numbers = heap_sort(random_numbers)
    
    print("Sorted List:", sorted_numbers)
