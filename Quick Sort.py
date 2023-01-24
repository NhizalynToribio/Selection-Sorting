print("************** PROGRAMMED BY: *****************")
print("************* NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("*************** Quick Sort  *******************")
print("**-------------------------------------------**")


# The whole program is about Quick Sorting
def quick_sort(mynumber, left, right):
    if left < right:
        partition_position = partition(mynumber, left, right)
        quick_sort(mynumber, left, partition_position - 1)
        quick_sort(mynumber, partition_position + 1, right)


def partition(mynumber, left, right):

    i = left
    j = right - 1
    pivot = mynumber[right]

    while i < j:

        while i < right and mynumber[i] < pivot:
            i += 1
        while j > left and mynumber[j] >= pivot:
            j -= 1
        if i < j:
            mynumber[i], mynumber[j] = mynumber[j], mynumber[i]

    if mynumber[i] > pivot:
        mynumber[i], mynumber[right] = mynumber[right], mynumber[i]

    print(mynumber)

    return i


mynumber = [62, 50, 95, 92, 24, 89, 15, 13, 8, 51]
print("\nThe Original Array List for Quick Sorting:\n", mynumber, "\n")

print("The Process of Quick Sorting:")
quick_sort(mynumber, 0, len(mynumber) - 1)

print("\nThe Final sorted Number using Quick Sorting:\n ", mynumber)

