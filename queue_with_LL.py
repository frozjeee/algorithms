from typing import overload
import linkedList

class Queue_LL:
    def __init__(self, size):
        self.size = size
        self.liveSize = 0
        self.LL = linkedList.linkedList()

    def enqueue(self, val):
        if self.liveSize == self.size:
            raise MemoryError("No more space")
        self.liveSize += 1
        self.LL.pushBack(val)

    def dequeue(self):
        try:
            self.LL.popFront()
        except:
            raise MemoryError("Queue is empty")

    def printQ(self):
        self.LL.printLL()


def main():
    a = Queue_LL(5)
    a.enqueue([1])
    a.enqueue("s")
    a.enqueue(3)
    a.enqueue(2)
    a.enqueue(1)  
    a.printQ()


if __name__ == "__main__":
    main()