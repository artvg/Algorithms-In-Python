# Quick Sort

import random

def in_place_partition(arr, low, high):
    # Choose random pivot index
    pivot_index = random.randint(low, high)

    # Move pivot to the end
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]  # Pivot value

    # Set up pointers
    left = low
    right = high - 1

    # Partitioning loop
    while left <= right:
        # Move left pointer if element < pivot
        while left <= right and arr[left] < pivot:
            left += 1
        # Move right pointer if element > pivot
        while right >= left and arr[right] > pivot:
            right -= 1
        # Swap elements if out of place
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    # Place pivot in correct position
    arr[left], arr[high] = arr[high], arr[left]

    # Return pivot index
    return left

def in_place_quick_sort(arr, low, high):
    if low >= high:
        return
    # Partition and sort recursively
    pivot_index = in_place_partition(arr, low, high)
    in_place_quick_sort(arr, low, pivot_index - 1)
    in_place_quick_sort(arr, pivot_index + 1, high)

# Test the algorithm
if __name__ == "__main__":
    S = [8, 3, 10, 5, 2, 7, 9]  # Unsorted list
    print("Unsorted List:", S)
    in_place_quick_sort(S, 0, len(S) - 1)
    print("Sorted List:", S)