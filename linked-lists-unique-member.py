import sys

class Node:
    
    def __init__(self):
        self.next = None
        self.data = ''


class LinkedList:

    def __init__(self):
        self.head = None

    def addToFront(self, obj):
        newNode = Node()
        newNode.data = obj
        newNode.next = self.head
        self.head = newNode 

    def isUniqueDict(self):
        foundDict = {}
        nextNode = self.head
        while nextNode != None:
            print("Value is {}".format(nextNode.data))  
            if foundDict.get(nextNode.data) != None:
                return False
            else:
                foundDict[nextNode.data] = 1                                
            nextNode = nextNode.next
        return True  

    def traverseListPartial(self, startNode):
        if startNode.next == None:
            return True
        seekValue = startNode.data
        nextNode = startNode.next
        while nextNode != None:
            if nextNode.data == seekValue:
                print("Found dups {} and {}".format(seekValue, nextNode.data))
                return False
            else:
                nextNode = nextNode.next  
        return True                       

    def isUniqueNoDataStructs(self):
        nextNode = self.head
        #foundDup = False
        while nextNode != None: # and foundDup == False:
            # Now loop through the rest of the list looking for a match  
            #print("Calling traverseListPartial")          
            if self.traverseListPartial(nextNode) == False:
                return False
            nextNode = nextNode.next

        return True            


def main():
    lnk = LinkedList()
    lnk.addToFront("abc")
    lnk.addToFront("vfc")
    lnk.addToFront("rca")
    lnk.addToFront("xyz")
    lnk.addToFront("rcc")   

    print("Listus uniqueus determinus")
    result = lnk.isUniqueDict()     
    print("All unique members") if result else print("Non-unique members found")

    print("Listus uniqueus determinus non structurus")
    result = lnk.isUniqueNoDataStructs()
    print("All unique members") if result else print("Non-unique members found")


if __name__ == '__main__':
    main()
            
        