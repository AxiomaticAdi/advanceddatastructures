from Node import Node


class StackLL(object):
    def __init__(self, list=None):
        self.top = None
        if list is not None:
            for item in list:
                self.add(item)

    def peek(self):
        return self.top.get_data() if self.top is not None else None

    def pop(self):
        # If empty stack, return None
        if self.top == None:
            return None

        # Save data in top
        temp = self.top.get_data()
        # If additional nodes after top, update pointer
        if self.top.get_next() is not None:
            self.top = self.top.get_next()
        # Else clear top pointer
        else:
            self.top = None

        # Return data in top
        return temp

    def push(self, data=None):
        # If no top, create
        if self.top == None:
            self.top = Node(data)
        # Otherwise, create new head pointing at old head
        else:
            temp = Node(data)
            temp.set_next(self.top)
            self.top = temp
        return

    def print(self):
        n = self.top
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        return True if self.top is None else False

    def clear(self):
        self.top = None


def main():
    s = StackLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.push(i)
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())
    while not s.is_empty():
        print(s.pop())


# Don't run main on import
if __name__ == "__main__":
    main()
