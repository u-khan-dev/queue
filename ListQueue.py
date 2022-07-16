from Node import Node


class ListQueue:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def is_empty(self):
        return not self.front

    def length(self):
        return self.size

    def enqueue(self, new_data):
        new_node = Node(new_data)

        if self.is_empty():
            self.front = new_node
        elif self.front.next is None:
            self.front.next = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

        self.size += 1

    def dequeue(self):
        if not self.is_empty():
            removed_node = self.front

            if not self.front.next:
                self.front = None
            elif self.front.next == self.back:
                self.front = self.back
                self.back = None
            else:
                self.front = self.front.next

            self.size -= 1

            removed_node.next = None
            return removed_node.value

    def get_front(self):
        if not self.is_empty():
            return self.front.value

    def print_queue(self):
        print()

        if self.is_empty():
            print('The queue is empty.')
        else:
            curr = self.front

            print('front: ', end='')

            while curr:
                if not curr.next:
                    arrow = ''
                else:
                    arrow = ' --> '

                print(curr.value + arrow, end='')
                curr = curr.next

        print()

