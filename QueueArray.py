class QueueArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.front = -1
        self.tail = -1

    def get_front(self):
        return self.array[self.front] if self.front >= 0 else None

    def get_tail(self):
        return self.array[self.tail] if self.front >= 0 else None

    def deq(self):
        # If empty, return none
        if self.front < 0:
            return None
        # Save value of front
        temp = self.array[self.front]
        # Update array
        if self.tail > self.front:
            self.array = self.array[1:]
            self.tail -= 1
        else:
            self.array = [0, 0, 0, 0, 0]
            self.front = -1
            self.tail = -1

        # Return value
        return temp

    def enq(self, data=None):
        # If array is full, double array size
        orig_size = len(self.array)
        if self.tail == orig_size - 1:
            new_size = orig_size * 2
            new_array = [0] * new_size
            new_array[:orig_size] = self.array
            self.array = new_array
        # Increment tail
        self.tail += 1
        # If first value, also increment front
        if self.front < 0:
            self.front += 1
        # Assign data
        self.array[self.tail] = data

    def print(self):
        for i in range(self.front, self.front + self.size(), 1):
            print(self.array[i % len(self.array)], "=>", end=" ")
        print("NULL")

    def is_empty(self):
        return True if self.front < 0 else None

    def clear(self):
        self.array = [0, 0, 0, 0, 0]
        self.front = -1
        self.tail = -1

    def is_full(self):
        l = self.size()
        return l >= len(self.array)

    def size(self):
        if self.front == -1:
            return 0
        l = self.tail - self.front + 1
        if self.tail < self.front:
            l = len(self.array) - self.front + self.tail + 1
        return l


def main():
    s = QueueArray()
    s.print()
    # print("Is empty?", s.is_empty())
    # for i in range(1, 4):
    #     s.enq(i)
    #     # print("Size:", s.size())
    #     # s.print()
    # s.print()
    # print("Deq: ", s.deq())
    # print("Deq: ", s.deq())
    # s.print()
    # for i in range(5, 11):
    #     s.enq(i)
    #     # print("Size:", s.size())
    #     # s.print()
    # print("Front:", s.get_front())
    # print("Tail: ", s.get_tail())
    # print("Deq:  ", s.deq())
    # s.print()
    # print("Is empty?", s.is_empty())
    # print("Size:", s.size())
    print(s.deq())
    s.enq(1)
    s.enq(2)
    s.enq(3)
    s.print()
    print(s.deq())
    print(s.deq())


# Don't run main on import
if __name__ == "__main__":
    main()
