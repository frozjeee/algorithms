class Stack:
    def __init__(self):
        self.stack = []
        self.max_vals = []

    def push(self, val):
        if (self.max_vals[-1] if self.max_vals else -1) <= val:
            self.max_vals.append(val)
        self.stack.append(val)

    def pop(self):
        if (self.max_vals[-1] if self.max_vals else -1) == self.stack.pop():
            self.max_vals.pop()
        self.stack.pop()

    def max(self):
        return self.max_vals[-1] if self.max_vals else "Empty stack"

def main():
    query_num = int(input())
    commands = []
    for _ in range(query_num):
        commands.append(input().strip().split())

    stack = Stack()
    for i in commands:
        if i[0] == "push":
            stack.push(int(i[1]))
        elif i[0] == "pop":
            stack.pop()
        elif [0] == "max":
            print(stack.max())
        else:
            print("unknown command")

if __name__ == "__main__":
    main()