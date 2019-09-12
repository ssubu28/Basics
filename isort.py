# Insertion Sort


def InsertionSort(alist):
    n = len(alist)

    for pos in range(1, n):
        i = pos - 1
        j = pos

        while alist[j] < alist[i] and i >= 0:  # i>=0 prevents list underflow
            # swap i and j and decrement i and j to check other elements in the sorted sublits. Checks from back to front.
            
            alist[i],alist[j] = alist[j],alist[i]
            i = i - 1
            j = j - 1

    return alist



alist =  raw_input("Enter a list of comma sep values: ").split(',')
print alist

alist = [int(x) for x in alist]

print "List before sotring: ", alist

print "List after sorting: ", InsertionSort(alist)
