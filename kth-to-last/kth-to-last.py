# Return kth-to-last: Implement algo to find the kth to last element of a singly linked list
class LinkedListNode:

    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return " -> ".join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            self.tail = self.head = LinkedListNode(value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail


llist = LinkedList()
llist.add(2)
llist.add(5)
llist.add(7)
llist.add(12)
llist.add(9)


def get_kth_to_last(k: int, llist: LinkedList):
    temp_arr = []
    current = llist.head

    if current.next == None:
        return llist.head
    else:
        temp_arr.append(current.value)
        while current.next:
            current = current.next
            temp_arr.append(current.value)
    return temp_arr[len(temp_arr) - k]


if __name__ == "__main__":
    print(f"Linked List: {llist}")
    print("Finding 2nd from last:", get_kth_to_last(2, llist))
    print("Finding 3rd from last:", get_kth_to_last(3, llist))
