print("************** PROGRAMMED BY: *****************")
print("************* NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("************* Selection Sort  *****************")
print("************** ---------- ********************")

# The whole program is about Selection Sorting
def sort(number):
    for n in range(len(number)-1,0,-1):
        for u in range(n):
            if number[u]>number