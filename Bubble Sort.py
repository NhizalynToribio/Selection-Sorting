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