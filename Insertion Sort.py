print("************** PROGRAMMED BY: *****************")
print("************* NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("*************** Insertion Sort  ****************")
print("**--------------------------------------------**")


# The whole program is about Insertion Sorting

def insertion_sort(mynumber):
    for i in range(1, len(mynumber)):
        j = i
        while mynumber[j - 1] > mynumber[j] and j > 0:
            mynumber[j - 1], mynumber[j] = mynumber[j], mynumber[j - 1]
            j -= 1
            print(mynumber)
