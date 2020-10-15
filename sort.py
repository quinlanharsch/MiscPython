import random


def swap(ls, a, b):
    ls[a], ls[b] = ls[b], ls[a]
    return ls


# ====== MERGESORT ======
#   /\  # Divide
#  /\/\
#  \/\/  # Conquer
#   \/
def mergesort(values):
    if len(values) > 1:
        # Divide
        mid = len(values) // 2
        left = mergesort(values[:mid])
        right = mergesort(values[mid:])

        # Conquer
        values = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:  # sorting component
                values.append(left.pop(0))
            else:
                values.append(right.pop(0))
        values += left
        values += right

    return values


# ====== QUICKSORT ======
#      .- _
#      . _ -
#    -_.  # Partition ad nauseum
# _-   .
def quicksort(arr, low, high):
    if low < high:
        pi = partition_and_sort(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)
    return arr


def partition_and_sort(values, low, high):
    i = low
    pivot = values[high]
    for j in range(low, high):
        if values[j] < pivot:
            i += 1
            swap(values, i-1, j)
    swap(values, i, high)
    return i


# ====== COUNTINGSORT ======
# 1 . 4   5   6
# 1 . 5   3   2
# 2 . 6   4   5
# 3 . 0   9   9
def counting_sort(in_arr, a_range):
    count_array = [0] * (a_range + 1)
    for i in in_arr:
        count_array[i] += 1
    for j in range(len(count_array)):
        count_array[j] += count_array[j-1]
    output_array = [0] * len(in_arr)
    for k in range(len(in_arr)):
        output_array[count_array[in_arr[k]] - 1] = in_arr[k]
        count_array[in_arr[k]] -= 1
    return output_array


if __name__ == '__main__':
    size = 10
    a_range = 2 * size
    in_arr = [random.randint(0, a_range) for _ in range(size)]
    ms_arr = in_arr.copy()
    qs_arr = in_arr.copy()
    cs_arr = in_arr.copy()
    print('in: ', in_arr)
    print('ms:', mergesort(ms_arr))
    print('qs: ', quicksort(qs_arr, 0, len(qs_arr) - 1))
    print('cs: ', counting_sort(cs_arr, a_range))
