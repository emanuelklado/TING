from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.data_queue = list()

    def __len__(self):
        return len(self.data_queue)

    def enqueue(self, value):
        self.data_queue.append(value)

    def dequeue(self):
        if len(self.data_queue) == 0:
            return None
        return self.data_queue.pop(0)

    def search(self, index):
        if index >= 0 and index < len(self.data_queue):
            return self.data_queue[index]
        else:
            raise IndexError("Index out of range")
            