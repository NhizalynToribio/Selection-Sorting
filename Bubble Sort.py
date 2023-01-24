print("************** PROGRAMMED BY: *****************")
print("************* NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("*************** Bubble Sort  *****************")
print("************** ---------- ********************")


# The whole program is about Bubble Sorting

def bubble_sort(mylist):
    for i in range(len(mylist) - 1, 0, -1):
        for j in range(i):
            if mylist[j] > mylist[j + 1]:
                temp = mylist[j]
                mylist[j] = mylist[j + 1]
                mylist[j + 1] = temp

                print(mylist)


mylist = [62, 50, 95, 92, 24, 89, 15, 13, 8, 51]
print("\nThe Original Array List for Bubble Sorting:\n", mylist, "\n")

print("The Process of Bubble Sorting:")
bubble_sort(mylist)

print("\nThe Final sorted Number using Bubble Sorting:\n ", mylist)
