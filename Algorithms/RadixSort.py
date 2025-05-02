# Radix Sort

def counting_sort_for_radix(arr, digit_place):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # for digits 0-9

    # Count occurrences of digits at current place
    for num in arr:
        digit = (num // digit_place) % 10
        count[digit] += 1

    # Convert count to cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // digit_place) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # Copy output back to original array
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know how many digits to process
    if len(arr) == 0:
        return

    max_num = max(arr)
    digit_place = 1

    # Apply counting sort to each digit
    while max_num // digit_place > 0:
        counting_sort_for_radix(arr, digit_place)
        digit_place *= 10

if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original Array:", data)
    radix_sort(data)
    print("Sorted Array:", data)
