class Queue():
    def __init__(self):
        self.queue = []


    '''Returns False if the queue has at least one element (length of list > 0). 
    Otherwise returns True (length of list == 0) '''
    def is_empty(self):
        return not len(self.queue)

    
    '''Adds an element to the end of the list (queue)'''
    def enqueue(self, element):
        self.queue.append(element)
        return self.queue


    '''Firstly checks if the queue is empty. If the queue does not empty, removes 
    the first element of the list (queue). Otherwise, it returns a warning message'''
    def dequeue(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.queue.pop(0)

    
    '''Return the value of the front of the queue without removing it. 
    If queue is empty return a warning message'''
    def peek(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.queue[0]
    

if __name__ == '__main__':
    my_queue = Queue()

    my_queue.enqueue("a")
    my_queue.enqueue("b")
    my_queue.enqueue("c")
    print(f"Queue first element: {my_queue.peek()}")
    # Queue first element: a
    
    print(f"The element '{my_queue.dequeue()}' removed from the Queue")
    # The element 'a' removed from the Queue

    print(f"Queue first element: {my_queue.peek()}")
    # Queue first element: b


     