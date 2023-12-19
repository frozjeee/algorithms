class MinHeap:
    def __init__(self):
        self.a = []


    def sort(self):
        b = []
        while len(self.a) != 0:
            g = self.delete_min()
            b.append(g)
        return b


    def add(self, val):
        self.a.append(val)
        i = len(self.a) - 1
        while i != 0:
            parent = (i - 2) // 2 if i % 2 == 0 else (i - 1) // 2

            if self.a[parent] > val:
                self.a[parent], self.a[i] = val, self.a[parent]
                i = parent
            else:
                break

        return self.a


    def search(self, val):
        pass


    def find_min(self):
        return self.a[0]


    def delete_min(self):
        ret = self.a[0]
        self.a[0] = self.a[-1]
        self.a.pop()
        i = 0
        while True:
            lf_child = 2 * i + 1 if 2 * i + 1 <= len(self.a) - 1 else None
            rgt_child = 2 * i + 2 if 2 * i + 2 <= len(self.a) - 1 else None
            if not lf_child and not rgt_child:
                break
            else:
                if (lf_child and rgt_child) and self.a[lf_child] > self.a[rgt_child]:
                    if self.a[rgt_child] < self.a[i]:
                        self.a[rgt_child], self.a[i] = self.a[i], self.a[rgt_child]
                        i = rgt_child
                    else:
                        break
                elif lf_child or self.a[lf_child] < self.a[rgt_child]:
                    if self.a[lf_child] < self.a[i]:
                        self.a[lf_child], self.a[i] = self.a[i], self.a[lf_child]
                        i = lf_child
                    else:
                        break
        return ret


a = MinHeap()

print(a.add(50))
print(a.add(30))
print(a.add(20))
print(a.add(15))
print(a.add(10))
print(a.add(8))
print(a.add(16))
print(a.add(60))
print(a.add(70))
print(a.sort())
