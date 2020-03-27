from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None

    def append(self, item):
        if self.storage.length == 0:
            print(item)
            self.storage.add_to_head(item)
            self.current = self.storage.head

        elif self.storage.length < self.capacity:
            print('1', item)
            self.storage.add_to_tail(item)
            self.current = self.current.next
            return
                        
        if self.storage.length >= self.capacity:
            print('2', item)
            if self.current == self.storage.tail:
                print('2.1', item)
                self.current = self.storage.head
                self.current.value = item
            else:
                print('2.2', item)
                self.current.next.value = item
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next
        

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
