from collections import deque

class Stack():
    def __init__(self):
        self.stack = deque()


    # return False if the stack has at list one element (len of stack > 0), otherwise returns True (len of stack = 0)
    def is_empty(self):
        return not len(self.stack)


    # add element at the end of the list (stack)
    def push(self, element):
        self.stack.append(element)
        return self.stack


    # remove the element from the end of the list (stack)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty."


    # Return the value of the element on the top of the stacjk without removing it.
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"


if __name__ == '__main__':
    my_stack = Stack()

    my_stack.push(100)
    my_stack.push(150)
    my_stack.push(200)

    print(f"Stack top: {my_stack.top()}")
    # Stack top: 200
    
    print(f"The element {my_stack.pop()} removed from the Stack")
    # The element 200 removed from the Stack
    
    print(f"Stack top: {my_stack.top()}")
    # Stack top: 150