from Node import Node

class LinkedList(object):
    def __init__(self, list=None):
        self.head = None
        if list is not None:
            for item in list:
                self.add(item)

    def get_head(self):
        if self.head == None:
            return None
        else:
            return self.head.get_data()

    def add(self, data):
        # If no head, create
        if self.head == None:
            self.head = Node(data)
        # Otherwise, create new head pointing at old head
        else:
            temp = Node(data)
            temp.set_next(self.head)
            self.head = temp
        return

    def search(self, data):
        # Start at head
        currentNode = self.head
        # Traverse through all nodes looking for data
        while currentNode is not None:
            if currentNode.get_data() == data:
                return True
            currentNode = currentNode.get_next()
        return False

    def delete(self, data):
        # If empty linked list, return None
        if self.head == None:
            return None
        # Start at head
        currentNode = self.head
        # Check if head needs to be deleted
        if currentNode.get_data() == data:
            self.head = currentNode.get_next()
            return currentNode.get_data()
        # Traverse & check remaining nodes
        while currentNode is not None and currentNode.get_next() is not None:
            # If next node contains data, update reference to skip
            if currentNode.get_next().get_data() == data:
                temp = currentNode.get_next()
                currentNode.set_next(currentNode.get_next().get_next())
                return temp.get_data()
            currentNode = currentNode.get_next()
        return None

    def print(self):
        n = self.head
        while n is not None:
            print(n.get_data(), "=>", end=" ")
            n = n.get_next()
        print("NULL")

    def is_empty(self):
        return self.head == None

    def clear(self):
        self.head = None


def main():
    l = list(range(1, 5))
    l.reverse()
    ll = LinkedList(l)
    ll.print()
    print("Search 4: ", ll.search(4))
    print("Search 5: ", ll.search(5))
    print("Delete 5: ", ll.delete(5))
    print("Delete 4: ", ll.delete(4))
    ll.print()
    print("Delete 1: ", ll.delete(1))
    ll.print()


# Don't run main on import
if __name__ == "__main__":
    main()
