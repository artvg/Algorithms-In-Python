# Merge Sort

def merge_sort(array):
    # If the array is 1 or 0 elements it returns the sorted array
    if len(array) <= 1:
        return array
        
    # Finds the middle index
    mid = len(array) // 2
    
    # Sorts the two halves
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])
    
    # Merges the two sorted halves
    return merge(left_half, right_half)
    
def merge(left, right):
    sorted_array = [] # Stores the merged result
    i = j = 0 # Pointers for both halves
    
    # This will compare elements from both halves, to then merge them in order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
            
    # Add any remainng elements from both halves
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array
    
# List to test the code 
A = [1, 99, 60, 6, 81, 42, 21, 92, 70, 4]
sorted_a = merge_sort(A)
print("Sorted Array:", sorted_a)
