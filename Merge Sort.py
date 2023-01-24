print("************** PROGRAMMED BY: *****************")
print("************* NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("*************** Merge Sort  *******************")
print("**-------------------------------------------**")


# The whole program is about Merge Sorting

def merge_sort(array):
    if len(array) > 1:
        left_array = array[:len(array) // 2]
        right_array = array[len(array) // 2:]

        merge_sort(left_array)
        merge_sort(right_array)

        # Merging left and right array
        #  i, j, k are the index of left and right array
        i = 0
        j = 0
        k = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1

        # Prints out the Process of Merge Sort
        print("The Left Array:", left_array)
        print("The Right Array:", right_array)


mynumber = [62, 50, 95, 92, 24, 89, 15, 13, 8, 51]
print("\nThe Original Array List for Merge Sorting:\n", mynumber, "\n")

print("The Process of Merge Sorting:")
merge_sort(mynumber)

print("\nThe Final sorted Number using Merge Sorting:\n ", mynumber)



