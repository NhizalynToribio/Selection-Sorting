print("************** PROGRAMMED BY: *****************")
print("************* NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("*************** Quick Sort  *******************")
print("**-------------------------------------------**")


# The whole program is about Quick Sorting
def quick_sort(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        pivot = seq.pop()

    greater_value = []
    lower_value = []

    for item in seq:
        if item > pivot:
            greater_value.append(item)

        else:
            lower_value.append(item)

    return quick_sort(lower_value) + [pivot] + quick_sort(greater_value)


print(quick_sort([62, 50, 95, 92, 24, 89, 15, 13, 8, 51]))


