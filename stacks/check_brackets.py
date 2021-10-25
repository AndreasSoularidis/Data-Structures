
class Stack():
    def __init__(self):
        self.stack = []


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

    def __str__(self):
        return self.stack[-1]

if __name__ == '__main__':
    my_stack = Stack()
    
    user_input = input("Please give a string: ")

    for char in user_input:
        if char in "[({":
            my_stack.push(char)
        
        if char in "])}":
            left = my_stack.pop()
            right = char
            # Check if match 
            if (left + right) not in ["()", "[]", "{}"]:
                print("Failure")
                break
    else:
        # Check if the stack is empty
        if my_stack.is_empty():
            print("Success")
        else:
            print("Failure")

# input: []
# output: Success

# input: [()]
# output: Success

# input: (())
# output: Success

# input: ({)
# output: Failure