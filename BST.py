import math
import queue


class Node(int):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)
    

class BST:
    def __init__(self):
        self.root = None
    
    def add(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            self.__add(val, self.root)

    def __add(self, val, node):
        if val < node.val:
            if node.left is not None:
                self.__add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self.__add(val, node.right)
            else:
                node.right = Node(val)

    def height(self):
        if self.root == None:
            return 0
        return max(self.__height(self.root.left), self.__height(self.root.right))

    def __height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__height(node.left), self.__height(node.right))

    def size(self):
        if self.root == None:
            return 0
        return self.__size(self.root)

    def __size(self, node):
        if node == None:
            return 0
        return 1 + self.__size(node.left) + self.__size(node.right)

    def printTreeDFS(self):
        if self.root != None:
            self.__printTreeDFS(self.root)
        else:
            print("Empty tree")
        
    def __printTreeDFS(self, node):
        # preOrder 
        if node != None:
            self.__printTreeDFS(node.left)
            self.__printTreeDFS(node.right)
            print(node.val)

        return

    def printTreeBFS(self):
        q = queue.Queue(int(math.pow(2, self.height())))
        q.enqueue(self.root)
        if self.root != None:
            while not q.isEmpty():
                node = q.dequeue()
                print(node.val)
                if node.left:
                    q.enqueue(node.left)
                if node.right:
                    q.enqueue(node.right)
        else:
            print("Empty tree")
        
    def reverse(self):
        if self.root != None:
            self.__reverse(self.root)
        else:
            print("Empty tree")

    def __reverse(self, node):
        if node != None:
            if node.left or node.right:
                self.__reverse(node.left)
                self.__reverse(node.right)
                node.left, node.right = node.right, node.left
        else:
            return

    def getChildren(self, val):
        if self.root != None:
            return self.__getChildren(self.root, val)
        else:
            print("Empty tree")

    def __getChildren(self, node, val):
        if node != None:
            print(node.val)
            if node.val == val:
                print("ik gere")
                return [f"left: {node.left if node.left else ''}, right: {node.right if node.right else ''}"]
            elif node.val < val:
                return self.__getChildren(node.left, val)
            else:
                return self.__getChildren(node.right, val)
        else:
            return


    def prettyPrintTree(self):
        if not self.root:
            print("Empty Tree")
            return
        self._prettyPrintTree(self.root)


    def _prettyPrintTree(self, node, prefix="", isLeft=True):
        

        if node.right:
            self._prettyPrintTree(node.right, prefix + ("│   " if isLeft else "    "), False)

        print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

        if node.left:
            self._prettyPrintTree(node.left, prefix + ("    " if isLeft else "│   "), True)
        

def main():
    a = BST()
    a.add(5)
    a.add(3)
    a.add(7)
    a.add(4)
    a.add(6)
    a.add(8)
    a.add(2)
    a.add(1)
    a.printTreeDFS()
    # a.reverse()
    # print("-----")
    # a.printTreeDFS()
    a.prettyPrintTree()
if __name__ == "__main__":
    main()