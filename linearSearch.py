# Program to search for a given key value in a list of integers
class searchListClass():
    def __init__(self, n, key):
        self.n = n
        self.key = key

    def searchList(self):
        for i in range(0,len(self.n)):
            if self.n[i] == self.key:
                return 1
        return -1

    def printLst(self):
        print self.n


obt = searchListClass([20,92,112,78,3], 12)

print obt.printLst()

if obt.searchList() == -1:
    print 'Key not found'
else:
    print 'Key found'
