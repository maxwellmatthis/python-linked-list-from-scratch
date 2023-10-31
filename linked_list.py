from typing import *


class Node:
    data: int
    next: Optional[Self]

    def __init__(self, number):
        self.data = number
        self.next = None

    def __str__(self):
        return str(self.data)

    def greater_than(self, other: Self):
        return self.data > other.data


def OutOfBoundsException(index):
    return Exception(f"Index {index} out of bounds!")


class LinkedList:
    root: Optional[Node]
    size: int

    def __init__(self, regular_list: None | list = None) -> None:
        self.root = None
        self.size = 0
        if regular_list is not None:
            for x in regular_list:
                self.add(x)

    def __len__(self) -> int:
        return self.size

    def __iter__(self):
        if self.root is None:
            return

        current = self.root
        while current.next != None:
            yield current.data
            current = current.next
        yield current.data

    def __str__(self) -> str:
        output = "["
        for x in self:
            output += str(x) + ", "
        output = output[:-2]  # <- remove last ", "
        return output + "]"

    def __get_node(self, index) -> Node | None:
        if index < 0:
            return None

        current = self.root
        for _ in range(index):
            if current.next:
                current = current.next
            else:
                return None
        return current

    def __getitem__(self, index) -> None | int:  # Node.data
        node = self.__get_node(index)
        if node is None:
            return None
        return node.data

    def __setitem__(self, index, value) -> None:
        node = self.__get_node(index)
        if node is None:
            raise OutOfBoundsException(index)
        node.data = value

    def add(self, value, index: None | int = None) -> None:
        """
        Adds an element at to the list and returns `None`.
        If no index is specified or the index is too large, the element will be added to the end.
        """
        if (index is None) or index > len(self) + 1:
            index = len(self)

        new = Node(value)

        if index == 0:
            new.next = self.root if self.root is not None else None
            self.root = new
        else:
            parent = self.__get_node(index - 1)
            new.next = parent.next
            parent.next = new

        self.size += 1

    def remove(self, index) -> None | int:  # Node.data
        """
        Removes an element from the list and returns it if the element exists.
        """
        if (self.root is None):
            return None

        removed = None
        if index == 0:
            removed = self.root
            self.root = self.root.next
        else:
            parent = self.__get_node(index - 1)
            removed = parent.next
            parent.next = removed.next

        self.size -= 1
        return removed.data

    def sort(self) -> None:
        """
        Sorts the list (least to greatest) and returns `None`.
        """
        if self.root.next is None:
            return None

        for e in range(len(self)):
            parent: Node = None
            current: Node = self.root
            for _ in range(len(self) - e):
                next = current.next
                if next is None:
                    break
                elif current.greater_than(next):
                    current.next = next.next
                    next.next = current
                    if parent is not None:
                        parent.next = next
                    else:
                        self.root = next
                    # current stays current
                    parent = next
                else:
                    parent = current
                    current = next

# --- Tests ---


ll = LinkedList([5, 4, 3])
assert "[5, 4, 3]" == str(ll)

ll.add(1)
ll.add(10, 0)
ll.add(3, 2)
ll.add(6, 100)
assert "[10, 5, 3, 4, 3, 1, 6]" == str(ll)
assert 7 == len(ll)
assert 3 == ll[4]
assert None == ll[100]

ll[1] = 8
assert 8 == ll[1]

try:
    ll[100] = 1
    assert False
except:
    pass

ll.remove(3)
assert "[10, 8, 3, 3, 1, 6]" == str(ll)

all = []
for x in ll:
    all.append(x)
assert "[10, 8, 3, 3, 1, 6]" == str(all)

ll.sort()
assert "[1, 3, 3, 6, 8, 10]" == str(ll)

assert 6 == len(ll)
