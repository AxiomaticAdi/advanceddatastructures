from Node import Node


class QueueLL(object):
    def __init__(self, list=None):
        self.front = None
        self.tail = None
        if list is not None:
            for item in list:
                self.enq(item)

    def get_front(self):
        return self.front.get_data() if self.front is not None else None

    def get_tail(self):
        return self.tail.get_data() if self.tail is not None else None

    def deq(self):
        # If empty, return none
        if self.front == None:
            return None
        # Else save value of front as temp
        temp = self.front.get_data()
        # Reassign front to next node
        self.front = self.front.get_next()
        # Return saved value
        return temp

    def enq(self, data=None):
        # If no head, create
        if self.front == None:
            self.front = Node(data)
            self.tail = self.front
        # Otherwise, add to back of queue
        else:
            temp = Node(data)
            self.tail.set_next(temp)
            self.tail = temp
        return

    def print(self):
        n = self.front
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        return True if self.front is None else False

    def clear(self):
        self.front = None
        self.tail = None


def main():
    s = QueueLL()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 7):
        s.enq(i)
    s.print()
    # print("Peek:", s.peek()) <- THIS IS A BUG - no peek function in this code
    print("Deq: ", s.deq())
    s.print()
    print("Is empty?", s.is_empty())


# Don't run main on import
if __name__ == "__main__":
    main()
