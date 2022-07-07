class Node:
    def __init__(self, key = None, next = None, prev = None): 
        self.key = key
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(f"data: {self.key}")

class linkedList: 
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, data):
        newNode = Node(data)
        if self.head != None:
            self.head.prev = newNode
        newNode.next = self.head    
        self.head = newNode
        if self.tail == None:
            self.tail = self.head

    def popFront(self):
        if self.head == None:
            raise Exception("LL is empty")
        if self.head.next:
            self.head.next.prev = None
        self.head = self.head.next
        if self.head == None:
            self.tail = None

    def pushBack(self, data):
        newNode = Node(data)
        if self.tail == None:
            self.tail = newNode
            self.head = self.tail
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        
    def popBack(self):
        if self.head == None:
            raise Exception("LL is empty")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

            
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
        newNode.prev = current
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
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        else:
            while counter != index:
                if current.next == None:
                    raise Exception("Out of range")
                counter += 1
                current = current.next
            current.prev.next = newNode
            current.prev = newNode
            newNode.next = current
            newNode.prev = current.prev


    def printLL(self):
        current = self.head
        while(current):
            print(current)
            print(f"--next: {current.next}--")
            print(f"--prev: {current.prev}--")
            print(f"--tail: {self.tail}--")
            print(f"--head: {self.head}--")
            current = current.next



a = linkedList()
a.pushFront(2)
a.pushBack(3)
a.pushBack(5)
a.pushBack(4)
# a.popBack()
# a.addAfter(0, 6)
a.addBefore(2, 9)

a.printLL()