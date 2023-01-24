print("************** PROGRAMMED BY: *****************")
print("************* NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("*************** Quick Sort  *******************")
print("**-------------------------------------------**")


# The whole program is about Quick Sorting
def quick_sort(array, left, right):
    if left < right:
        partition_position = partition(array, left, right)
        quick_sort(array, left, partition_position - 1)
        quick_sort(array, partition_position + 1, right)


def partition(array, left, right):

    i = left
    j = right - 1
    pivot = array[right]

    while i < j:

        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] >= pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]

    print(array)

    return i


mynumber = [62, 50, 95, 92, 24, 89, 15, 13, 8, 51]
print("\nThe Original Array List for Quick Sorting:\n", mynumber, "\n")


print("\nThe Final sorted number using Quick Sort: \n",
      quick_sort([62, 50, 95, 92, 24, 89, 15, 13, 8, 51]))


