class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, new_value):
        self.value = new_value

    def setNext(self, new_next):
        self.next = new_next

    def __str__(self):
        return "{}".format(self.value)

    __repr__ = __str__


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert(self, after, item):
        newNode = Node(item)
        current = self.head
        while current.getValue() != after:
            current = current.getNext()
        current.next, newNode.next = newNode, current.next
        self.count += 1

    def pop(self):
        last = self.tail
        current = self.head
        for i in range(self.count - 2):
            current = current.next
        del current.next
        self.tail = current
        current.setNext(None)
        self.count -= 1
        return last

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        elif self.tail == self.head:
            self.tail = Node(value)
            self.head.setNext(self.tail)
        else:
            new_node = Node(value)
            current = self.head
            for i in range(self.count - 1):
                current = current.next
            current.setNext(new_node)
            self.tail = new_node
        self.count += 1

    def remove(self, value):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getValue() == value:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous is None:
            self.head = current.getNext()
        elif current.getNext() is None:
            self.tail = previous
            previous.setNext(None)
        else:
            previous.setNext(current.getNext())

        self.count -= 1

    def isEmpty(self):
        return self.head is None

    def size(self):
        return self.count

    def add(self, value):
        new_node = Node(value)
        new_node.setNext(self.head)
        self.head = new_node
        self.count += 1

        if self.size() == 1:
            self.tail = new_node

    def search(self, value):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getValue() == value:
                return True
            else:
                current = current.getNext()
        return found

    def printList(self):
        temp = self.head
        for i in range(self.count):
            print(temp.value, end=' ')
            temp = temp.next
        print()
