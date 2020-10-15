from singly_linked_list import *


class HashTable():
    def __init__(self, length):
        self.table = []
        for i in range(length):
            self.table.append(SLinkList())
        self.length = length

    def __len__(self):
        return self.length

    def hash(self, data):
        return data % self.length

    def add(self, data):
        self.table[self.hash(data)].add(data)

    def delete(self, data):
        self.table[self.hash(data)].delete(data)

    def search(self, data):
        return self.table[self.hash(data)].search(data)

    def __str__(self):  # dirty print
        return str([str(i) for i in self.table])


if __name__ == '__main__':
    ls = HashTable(4)
    ls.add(1)
    ls.add(5)
    ls.add(9)
    ls.add(0)
    ls.delete(5)
    a = ls.search(0)
    print(a)
    print(ls)
