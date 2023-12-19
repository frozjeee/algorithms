# queue with arrays, not linked list
class Queue:
    def __init__(self, size):
        self.read = 0
        self.write = 0
        self.size = size
        self.arr = []
        for _ in range(size):
            self.arr.append(" ")

    def enqueue(self, value):
        if self.write == self.read - 1:
            raise Exception("need space")
        else:
            if self.write == self.size:
                if self.read > 1:
                    self.write = 0
                    self.arr.pop(self.write)
                    self.arr.insert(self.write, value)
                    self.write += 1
                else:
                    raise Exception("Need space")
            else:
                self.arr.pop(self.write)
                self.arr.insert(self.write, value)
                self.write += 1
    
    def dequeue(self):
        if self.read == self.size:
            self.read = 0
            toReturn = self.arr.pop(self.read)
            self.arr.insert(self.read, " ")
            self.read += 1
            return toReturn
        else:
            if self.read == self.write:
                raise Exception("List is empty")
            toReturn = self.arr.pop(self.read)
            self.arr.insert(self.read, " ")
            self.read += 1
            return toReturn

    def getFront(self):
        return self.arr[self.read] if self.arr[self.read] != " " else None

    def isEmpty(self):
        if self.read == self.write:
            return True
        return False

    def printQ(self):
        print(self.arr)


if __name__ == "__main__":
    a = Queue(5)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(4)
    a.enqueue(4)
    a.enqueue(4)
    a.dequeue()
    a.dequeue()
    a.enqueue(5)
    a.dequeue()
    a.enqueue(6)
    a.dequeue()
    a.dequeue()
    a.dequeue()
    a.dequeue()
    print(a.write, a.read)
    # a.enqueue(3)
    a.printQ()