# Approach 1: O(n log n)

def sort_into_peaks_and_valleys1(array: list[int]) -> list[int]:
    sorted_array = sorted(array)
    middle_index = len(array) // 2

    # Integers in the first half of the sorted array, which are smaller, will be used as valleys
    # Integers in the second half of the sorted array, which are larger, will be used as peaks

    i = 0
    j = middle_index

    result = []
    next_element_should_be_peak = True

    while i < middle_index or j < len(array):
        if next_element_should_be_peak:
            result.append(sorted_array[j])
            j += 1
        else:
            result.append(sorted_array[i])
            i += 1

        next_element_should_be_peak = not next_element_should_be_peak

    return result



# Approach 2: O(n log n)

def sort_into_peaks_and_valleys2(array: list[int]) -> list[int]:
    sorted_array = sorted(array)

    for i in range(1, len(sorted_array), 2):
        sorted_array[i], sorted_array[i - 1] = sorted_array[i - 1], sorted_array[i]

    return sorted_array



# Approach 3: O(n)

def sort_into_peaks_and_valleys3(array: list[int]) -> list[int]:
    for i in range(1, len(array), 2):  # For each index where there should be a peak
        if array[i] >= max(array[i-1], array[i + 1]):  # Already a peak
            continue

        if array[i + 1] > array[i - 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
        else:
            array[i - 1], array[i] = array[i], array[i - 1]

    return array




if __name__ == '__main__':
    array = [3, 4, 2, 1, 9, 8, 7]

    print(sort_into_peaks_and_valleys3(array))