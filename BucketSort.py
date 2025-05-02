# Bucket Sort

def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Create empty buckets
    num_buckets = len(arr)
    max_val = max(arr)
    buckets = [[] for _ in range(num_buckets)]

    # Distribute elements into buckets
    for num in arr:
        index = (num * num_buckets) // (max_val + 1)
        buckets[index].append(num)

    # Sort each bucket and concatenate results
    sorted_arr = []
    for bucket in buckets:
        insertion_sort(bucket)
        sorted_arr.extend(bucket)

    return sorted_arr

if __name__ == "__main__":
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original Array:", data)
    sorted_data = bucket_sort(data)
    print("Sorted Array:", sorted_data)
