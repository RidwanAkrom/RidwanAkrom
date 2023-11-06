def find_occurrences(arr, x):
    def first_occurrence(arr, x):
        left, right = 0, len(arr) - 1
        first = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == x:
                first = mid
                right = mid - 1
            elif arr[mid] < x:
                right = mid - 1
            else:
                left = mid + 1

        return first

    def last_occurrence(arr, x):
        left, right = 0, len(arr) - 1
        last = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == x:
                last = mid
                left = mid + 1
            elif arr[mid] < x:
                right = mid - 1
            else:
                left = mid + 1

        return last

    first_index = first_occurrence(arr, x)
    last_index = last_occurrence(arr, x)

    if first_index != -1:
        return list(range(first_index, last_index + 1))
    else:
        return []

# Example usage:
sorted_list = [10, 8, 6, 6, 6, 4, 4, 2, 2, 1]
x = 6
result = find_occurrences(sorted_list, x)
print(result)  # Output: [2, 3, 4]
