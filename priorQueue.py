class PriorQueue:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.H = []
        self.size = 0

    def __repr__(self):
        return ", ".join([str(i) for i in self.H])

    def leftChild(self, index):
        if index == 0:
            return 1
        return index*2 + 1

    def rightChild(self, index):
        if index == 0:
            return 2
        return index*2 + 2

    def parent(self, index):
        if index % 2 == 0:
            return int(index/2) - 1
        return int(index/2)

    def getMax(self):
        return self.H[0]

    def insert(self, val):
        if self.size == self.maxSize:
            raise MemoryError("Out of memory")
        self.size += 1
        self.H.append(val)
        self.siftUp(self.size - 1)

    def extractMax(self):
        result = self.H[0]
        self.H[0] = self.H[self.size - 1]
        self.H.pop()
        self.size -= 1
        self.siftDown(0)
        return result

    def remove(self, index):
        self.H[index] = float('inf')
        self.siftUp(index)
        self.extractMax()   

    def changePrior(self, index, val):
        oldVal = self.H[index]
        self.H[index] = val
        if val > oldVal:
            self.siftUp(index)
        else:
            self.siftDown(index)

    def siftUp(self, index):
        while index > 0 and self.H[self.parent(index)] < self.H[index]:
            parent = self.parent(index)
            self.H[index], self.H[parent] = self.H[parent], self.H[index]
            index = parent

    def siftDown(self, index):
        maxIndex = index
        l = self.leftChild(maxIndex)
        if l <= self.size - 1 and self.H[l] > self.H[maxIndex]:
            maxIndex = l
        r = self.rightChild(maxIndex)
        if r <= self.size - 1 and self.H[r] > self.H[maxIndex]:
            maxIndex = r
        if index != maxIndex:
            self.H[index], self.H[maxIndex] = self.H[maxIndex], self.H[index]
            self.siftDown(maxIndex)


def main():
    a = PriorQueue(10)
    a.insert(20)
    print(a)
    a.insert(15)
    print(a)
    a.insert(12)
    print(a)
    a.insert(5)
    print(a)
    a.extractMax()
    print(a)
    a.insert(50)
    print(a)
    a.insert(16)
    print(a)


if __name__ == "__main__":
    main()