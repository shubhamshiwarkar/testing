class MyStack:
    def __init__(self):
        self.stack = []
    
    def add(self, data):
        self.stack.append(data)
    
    def remove(self):
        return self.stack.pop()
    
    def top(self):
        return print(self.stack[-1], '<-- top')
    
    def isEmpty(self):
        return self.size() == 0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print(self.stack[-1], '<-- top')
        for i in self.stack[-2::-1]:
            print(i)
        print('')


if __name__ == '__main__':
    myStack = MyStack()
    myStack.add(1)
    myStack.add(2)
    myStack.add(3)
    myStack.add(4)
    myStack.add(5)

    myStack.display()

    myStack.remove()
    myStack.display()

    myStack.remove()
    myStack.display()

    myStack.top()