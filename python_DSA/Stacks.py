class Stacks:
    def __init__(self):
        self.stack = []

    def add(self, data):
        self.stack.append(data)

    def remove(self):
        if self.isEmpty():
            return
        else:
            self.stack.pop()

    def top(self):
        return print(self.stack[-1], "\n")

    def isEmpty(self):
        if self.stack == []:
            return True

    def display(self):
        if self.isEmpty():
            return
        else:
            print(self.stack[-1], "<--top")
            for i in self.stack[-2::-1]:
                print(i)
            print("")


if __name__ == "__main__":
    s = Stacks()

    s.add(3)
    s.add(78)
    s.add(34)
    s.add(98)

    s.display()

    s.remove()
    s.display()

    s.remove()
    s.display()

    s.add(23)
    s.display()

    s.remove()
    s.display()

    s.remove()
    s.display()

    s.remove()
    s.display()
