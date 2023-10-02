class StackArray(object):
    def __init__(self, size=5):
        self.array = [0 for i in range(size)]
        self.top = -1

    def peek(self):
        # If no values in array, return none
        if self.top < 0:
            return None
        else:
            return self.array[self.top]

    def pop(self):
        # If no values in array, return none
        if self.top < 0:
            return None
        else:
            # Save value
            temp = self.array[self.top]
            # Move top
            self.top -= 1
            # Return saved value
            return temp

    def push(self, data=None):
        # If array is full, double array size
        orig_size = len(self.array)
        if self.top == orig_size - 1:
            new_size = orig_size * 2
            new_array = [0] * new_size
            new_array[:orig_size] = self.array
            self.array = new_array
        # Increment top
        self.top += 1
        # Assign data
        self.array[self.top] = data

    def print(self):
        for i in range(self.top, -1, -1):
            print(self.array[i], "=>", end=" ")
        print("NULL")

    def is_empty(self):
        return True if self.top < 0 else False

    def is_full(self):
        return self.top == len(self.array) - 1

    def clear(self):
        self.top = -1

    def size(self):
        return self.top + 1


def main():
    s = StackArray()
    s.print()
    print("Is empty?", s.is_empty())
    for i in range(1, 10):
        s.push(i)
    s.print()
    print("Peek:", s.peek())
    print("Pop: ", s.pop())
    s.print()
    print("Is empty?", s.is_empty())
    # print(s.peek())
    # print(s.is_empty())
    # s.push(1)
    # s.print()
    # print(s.pop())
    # s.print()
    # s.push(2)
    # s.print()
    # print(s.peek())
    # print(s.is_empty())


# Don't run main on import
if __name__ == "__main__":
    main()
