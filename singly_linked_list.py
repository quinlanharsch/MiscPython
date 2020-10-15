class SLinkList(object):
    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        node = Node(data)
        node.set_next(self.head)
        self.head = node

    def __len__(self):
        pointer = self.head
        count = 0
        while pointer:  # is not null
            count += 1
            pointer = pointer.get_next()
        return count

    def search(self, data):
        pointer = self.head
        while pointer:  # is not null
            if pointer.get_data() == data:
                return pointer
            pointer = pointer.get_next()
        # if not found
        return pointer

    def delete(self, data):
        p = self.head
        tp = None
        while p:  # is not null
            if p.get_data() == data:
                tp.set_next(p.get_next())
                del p
                return True
            tp = p
            p = p.get_next()
        # if not found
        return False

    def __str__(self):  # if printed
        p = self.head
        m = []
        while p:
            m.append(p.get_data())
            p = p.get_next()
        return "{" + str(m)[1:]


class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

