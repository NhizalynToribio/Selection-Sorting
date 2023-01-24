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
