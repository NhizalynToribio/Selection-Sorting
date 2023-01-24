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


    for item in seq:
        if item > pivot:
            greater_value.append(item)

        else:
            lower_value.append(item)

    return quick_sort(lower_value) + [pivot] + quick_sort(greater_value)


mynumber = [62, 50, 95, 92, 24, 89, 15, 13, 8, 51]
print("\nThe Original Array List for Quick Sorting:\n", mynumber, "\n")


print("\nThe Final sorted number using Quick Sort: \n",
      quick_sort([62, 50, 95, 92, 24, 89, 15, 13, 8, 51]))


