print("************** PROGRAMMED BY: *****************")
print("************* NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("************* Selection Sort  *****************")
print("************** ---------- ********************")


# The whole program is about Selection Sorting
def selection_sort(number):

    for n in range(9):
        minpos = n
        for u in range(n, 10):
            if number[u] < number[minpos]:
                minpos = u

        temp = number[n]
        number[n] = number[minpos]
        number[minpos] = temp

        print(number)


number = [62, 50, 95, 92, 24, 89, 15, 13, 8, 51]
print("\nThe Original Array List for Selection Sorting:\n", number, "\n")

print("The Process of Selection Sorting:")
selection_sort(number)

print("\nThe Final sorted Number using Selection Sorting:\n ", number)
