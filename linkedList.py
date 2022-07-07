class Node:
    def __init__(self, key = None, next=None): 
        self.key = key
        self.next = next

    def __str__(self):
        return str(self.key)

class linkedList: 
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, data):
        newNode = Node(data)
        newNode.next = self.head    
        self.head = newNode
        if self.tail == None:
            self.tail = self.head

    def popFront(self):
        if self.head == None:
            raise Exception("LL is empty")
        self.head = self.head.next
        if self.head == None:
            self.tail = None


    def pushBack(self, data):
        newNode = Node(data)
        if self.tail == None:
            self.tail = newNode
            self.head = self.tail
        else:
            self.tail.next = newNode
            self.tail = newNode
        
    def popBack(self):
        if self.head == None:
            raise Exception("LL is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
            self.tail = current
            
    def addAfter(self, index, data):
        if self.head == None:
            raise Exception("LL is empty")
        newNode = Node(data)
        counter = 0
        current = self.head
        while counter != index:
            if current.next == None:
                raise Exception("Out of range")
            counter += 1
            current = current.next
        newNode.next = current.next
        current.next = newNode
        if self.tail == current:
            self.tail = newNode

    def addBefore(self, index, data):
        if self.head == None:
            raise Exception("LL is empty")
        newNode = Node(data)
        counter = 0
        current = self.head
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            while counter != index:
                if current.next == None:
                    raise Exception("Out of range")
                if counter + 1 == index:
                    break
                counter += 1
                current = current.next
            newNode.next = current.next
            current.next = newNode
            if self.head == current.next:
                self.head = newNode


    def printLL(self):
        current = self.head
        while(current):
            print(current.key, end=" ")
            current = current.next


def main():
    a = linkedList()
    a.pushFront(2)
    a.pushBack(3)
    a.pushBack(5)
    a.pushBack(4)
    a.addAfter(3, 6)
    a.addBefore(0, 9)
    a.printLL()


if __name__ == "__main__":
    main()