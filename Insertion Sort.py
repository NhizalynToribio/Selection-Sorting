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


mynumber = [62, 50, 95, 92, 24, 89, 15, 13, 8, 51]
print("\nThe Original Array List for Insertion Sorting:\n", mynumber, "\n")

print("The Process of Insertion Sorting:")
insertion_sort(mynumber)

print("\nThe Final sorted Number using Insertion Sorting:\n ", mynumber)

