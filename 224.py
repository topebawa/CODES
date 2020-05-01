class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        val = str(self.value)
        prev = str(self.prev.value) if self.prev != None else 'None'
        next = str(self.next.value) if self.next != None else 'None'
        return "Node with value " + val + ", prev " + prev + ", next "+next


class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self

    def insert(self, value, index):
        if index + 1 > self.length:
            return print('Index too Large')
        newNode = Node(value)
        currentNode = self.head
        i = 0
        while i < index:
            currentNode = currentNode.next
            i += 1
        newNode.next = currentNode
        newNode.prev = currentNode.prev
        currentNode.prev.next = newNode
        currentNode.prev = newNode
        self.length += 1
        return self

    def delete(self, index):
        if index + 1 > self.length:
            return print('Index too Large')
        currentNode = self.head
        i = 0
        while i < index:
            currentNode = currentNode.next
            i += 1
        if currentNode.prev == None:
            self.head = currentNode.next
        else:
            currentNode.prev.next = currentNode.next
        if currentNode.next == None:
            self.tail = currentNode.prev
        else:
            currentNode.next.prev = currentNode.prev
        self.length -= 1
        return self

    def printList(self, inverse=False):
        nodeList = []
        currentNode = self.head if inverse == False else self.tail
        nodeList.append(currentNode.value)
        print(currentNode)
        if inverse:
            while currentNode.prev != None:
                currentNode = currentNode.prev
                nodeList.append(currentNode.value)
                print(currentNode)
            print('From Tail to Head')
        else:
            while currentNode.next != None:
                currentNode = currentNode.next
                nodeList.append(currentNode.value)
                print(currentNode)
            print('From Head to Tail')
        print(nodeList)
        return self


myList = DoublyLinkedList(1)

myList.append(8)
myList.append(3)
myList.append(5)
myList.append(20)
myList.delete(4)
print(myList.printList(True))
