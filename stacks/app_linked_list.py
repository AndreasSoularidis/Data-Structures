''' Node class represents a node of the list '''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

'''' LnkedList class represents the linked list '''
class LinkedList:
    def __init__(self):
        self.head = None
    

    # Check if the list is empty or not
    def is_empty(self):
        return not self.head


    # Add a new node to the front of the linked list
    def push(self, new_node):
        if self.is_empty():
           self.head = new_node
        else:
            # Step 2: Link head with the new node
            new_node.next = self.head
            self.head = new_node


    # Return the first node of the linked list
    def top(self):
        if self.is_empty():
            print("Error: List is empty")
            return 
        return self.head.value


    # Remove the first node of the linked list
    def pop(self):
        if self.is_empty():
            print("Error: List is empty")
            return

        self.head = self.head.next



if __name__ == '__main__':
    my_stack = LinkedList()
    
    my_stack.push(Node(100))
    my_stack.push(Node(150))
    my_stack.push(Node(200))

    print(f"Stack top: {my_stack.top()}")
    # Stack top: 200
    
    my_stack.pop()
    
    print(f"Stack top: {my_stack.top()}")
    # Stack top: 150
    