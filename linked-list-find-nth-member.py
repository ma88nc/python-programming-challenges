# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
# From Laakman-McDowell, "Cracking the Code Interview", 6th edition, problem 2.2, p. 94

# Additional notes: Note that for this solution, we have defined k such that passing in k = 1 would return the last element, k
# 2 would return to the second to last element, and so on. It is equally acceptable to define k such that k
# = e would return the last element.

import sys

class Node:
    
    def __init__(self):
        self.next = None
        self.data = ''


class LinkedList:

    def __init__(self):
        self.head = None

    def getListSize(self):
        current = self.head
        count = 1
        while current.next !=  None:
            count += 1
            current = current.next
        return count  

    def addFirst(self, data):
        newNode = Node()
        newNode.data = data               
        newNode.next = self.head
        self.head = newNode

    def traverseNItems(self, size, n):
        current = self.head
        count = 0
        while current.next != None and count < size - n - 1:
            print("Current data is {}".format(current.data))
            current = current.next
            count += 1
        return current.data     

    def traverseNItemsOnePass(self, n):
        current = self.head
        ptr2 = self.head
        count = 0
        while current.next != None:
            count += 1
            if count > n:
                ptr2 = ptr2.next
            current = current.next
        print(ptr2.data)
        return ptr2.data

def main():
    if len(sys.argv) < 2:
        print("Invoke with count")
        return

    n = int(sys.argv[1])  

    lnklst = LinkedList()
    lnklst.addFirst("apple")
    lnklst.addFirst("banana")
    lnklst.addFirst("cherry")
    lnklst.addFirst("kumquat")
    lnklst.addFirst("strawberry")  
    lnklst.addFirst("canteloupe")  
    lnklst.addFirst("orange")  
    lnklst.addFirst("pear")

    print("Linkus listus traversus countus")
    size = lnklst.getListSize()
    if n > size:
        print("Sorry, list has only {} members".format(size))
        return

    print("Linked list size is {}".format(size))
    foundData = lnklst.traverseNItems(size, n)
    print("Found data is {}".format(foundData))

    print("Linkus listus traversus countus one passus")
    foundData = lnklst.traverseNItemsOnePass(n)
    print("Found data is {}".format(foundData))

if __name__ == '__main__':
    main()