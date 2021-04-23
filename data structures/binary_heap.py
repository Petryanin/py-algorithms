from typing import List


class Heap:
    def __init__(self, *data):
        self.arr = []
        self.size = 0
        if not data:
            return
        else:
            for item in data:
                self.insert(item)

    def __str__(self):
        return str(self.arr)

    def sift_up(self, index):
        while index:
            parent = (index - 1) // 2
            if self.arr[index] < self.arr[parent]:
                self.arr[index], self.arr[parent] = self.arr[parent], self.arr[index]
                index = parent
            else:
                break

    def sift_down(self):
        if not self.size:
            return

        index = 0
        child_left = index * 2 + 1

        while child_left < self.size:
            child_right = index * 2 + 2

            if child_right >= self.size or self.arr[child_left] <= self.arr[child_right]:
                branch = child_left
            else:
                branch = child_right

            if self.arr[index] < self.arr[branch]:
                return

            self.arr[index], self.arr[branch] = self.arr[branch], self.arr[index]
            index = branch
            child_left = index * 2 + 1

    def insert(self, data):
        self.arr.append(data)
        self.size += 1
        self.sift_up(self.size - 1)

    def pop_min(self):
        if not self.size:
            return
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        self.size -= 1
        self.sift_down()
        return self.arr.pop()


def heap_sort(arr: list):
    heap = Heap(*arr)
    for i in range(heap.size):
        arr[i] = heap.pop_min()
