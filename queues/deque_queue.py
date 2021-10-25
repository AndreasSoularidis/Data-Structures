from collections import deque

class Queue():
    def __init__(self):
        self.queue = deque()


    ''' Return False if the queue has at list one element (len of queue > 0), 
    otherwise returns True (len of queue = 0) '''
    def is_empty(self):
        return not len(self.queue)


    ''' Add element to the end of the queue '''
    def enqueue(self, element):
        self.queue.append(element)
        return self.queue


    ''' Remove the element from the end of the queue.
    If the queue is empty returns a warning message'''
    def dequeue(self):
        if self.is_empty():
            return "Warning: The queue is empty"
        return self.queue.popleft()
        

    ''' Return the value of the element on the front of the queue without removing it.
    If the queue is empty returns a warning message '''
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