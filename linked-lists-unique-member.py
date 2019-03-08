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

    def traverseListDict(self):
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


def main():
    lnk = LinkedList()
    lnk.addToFront("abc")
    lnk.addToFront("vfc")
    lnk.addToFront("rca")
    lnk.addToFront("xyz")
    lnk.addToFront("rca")   

    print("Listus uniqueus determinus")
    result = lnk.traverseListDict()     
    print("All unique members") if result else print("Non-unique members found")

if __name__ == '__main__':
    main()
            
        