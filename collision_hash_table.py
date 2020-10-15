#TODO Everything here <3 T-T

class HashTable():
    def __init__(self, length, algorithm, probe):
        self.table = []
        assert algorithm.lower in ['cuckoo', 'open', 'double']
        self.algorithm = algorithm.lower
        assert probe.lower in ['linear', 'quadratic', 'double']
        self.probe = probe.lower

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
