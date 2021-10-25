''' Node class represents a node of the list '''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

'''' LnkedList class represents the linked list '''
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    

    ''' Check if the list (queue) is empty so returns True (self.head is None) 
    or not so returns False (self.head is not None) '''
    def is_empty(self):
        return not self.head


    '''Add a new node to the end of the linked list (queue)'''
    def enqueue(self, new_node):
        if self.is_empty():
           self.head = new_node
           self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    
    ''' Remove the first node of the linked list (queue).
    If the linked list (queue) is empty returns a warning message '''
    def dequeue(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        deleted_element = self.head.value
        self.head = self.head.next
        return deleted_element

    
    ''' Return the first node of the linked list. 
    If the linked list (queue) is empty returns a warning message'''
    def peek(self):
        if self.is_empty():
            return  "Warning: The queue is empty"
        return self.head.value


if __name__ == '__main__':
    my_queue = LinkedList()

    my_queue.enqueue(Node("a"))
    my_queue.enqueue(Node("b"))
    my_queue.enqueue(Node("c"))

    print(f"Queue first element: {my_queue.peek()}")
    # Queue first element: a
    
    print(f"The element '{my_queue.dequeue()}' removed from the Queue")
    # The element 'a' removed from the Queue

    print(f"Queue first element: {my_queue.peek()}")
    # Queue first element: b
