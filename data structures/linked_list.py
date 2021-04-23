class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, *data):
        self.head = None
        if data:
            for item in data:
                self.append(item)

    def __str__(self):
        res = '['
        curr = self.head
        if curr is None:
            res += ']'
            return res
        while curr.data is not None:
            res += str(curr.data)
            if(curr.next is not None):
                curr = curr.next
                res += ', '
            else:
                break
        res += ']'
        return res

    def length(self):
        curr = self.head
        if curr is None:
            return 0
        res = 1
        while curr.next is not None:
            curr = curr.next
            res += 1
        return res

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        if curr is None:
            self.head = new_node
            return
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def insert(self, index, data):
        curr = self.head
        if curr is None:
            return self.append(data)
        elif not 0 <= index < self.length():
            raise IndexError('Index out of range')

        if not index:
            new_node = Node(data)
            temp = self.head
            self.head = new_node
            new_node.next = temp
            return

        i = 0
        while i < index - 1:
            curr = curr.next
            i += 1
        new_node = Node(data)
        temp = curr.next
        curr.next = new_node
        new_node.next = temp

    def pop(self, index=None):
        curr = self.head
        index = self.length() - 1 if index is None else index

        if curr is None or not 0 <= index < self.length():
            raise IndexError('Index out of range')

        if not index:
            res = self.head.data
            self.head = self.head.next
            return res

        i = 0
        while i < index - 1:
            curr = curr.next
            i += 1
        res = curr.next.data
        curr.next = curr.next.next
        return res

    def get(self, index=None):
        if index is None or self.head is None or not 0 <= index < self.length():
            return None

        curr = self.head
        i = 0
        while i < index:
            curr = curr.next
            i += 1
        return curr.data

    def __cmp(self, first, second, reverse):
        return first < second if not reverse else first >= second

    def sort(self, reverse=False):
        if self.head is None:
            return

        curr = self.head
        while curr.next is not None:
            comp = curr.next
            while comp is not None:
                if self.__cmp(comp.data, curr.data, reverse):
                    comp.data, curr.data = curr.data, comp.data
                comp = comp.next
            curr = curr.next
            if curr is None:
                break
