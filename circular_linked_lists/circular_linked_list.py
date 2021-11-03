''' Node class represents a node of the list'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


''' CircularLinkedList class represents the circular linked list'''
class CircularLinkedList:
    def __init__(self):
        self.tail = None


    '''Returns True if the list is empty (so self.tail = None) 
    Otherwise, returns False'''
    def list_is_empty(self):
        return not self.tail

    
    ''' Add a new Node to the front of the circular linked list '''
    def add_to_front(self, new_node):
        if self.list_is_empty():
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node

    
    ''' Add a new Node at the end of the circular linked list '''
    def add_to_back(self, new_node):
        if self.list_is_empty():
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node


    ''' Remove the first Node of the circular linked list'''
    def remove_first(self):
        # List is already empty
        if self.list_is_empty():
            print("Warning: List is empty")
            return

        # List has exactly one node
        if self.tail.next == self.tail:
            self.tail.next = None
            self.tail = None
            return

        # List has more than one nodes
        first_node = self.tail.next
        second_node = first_node.next
        self.tail.next = second_node

    
    ''' Remove the last Node of the circular linked list'''
    def remove_last(self):
         # List is already empty
        if self.list_is_empty():
            print("Warning: List is empty")
            return

        # List has exactly one node
        if self.tail.next == self.tail:
            self.tail.next = None
            self.tail = None
            return
        
        # List has more than one nodes
        # Find the second to last node
        last_node = self.tail
        prev_to_last_node = last_node.next
        while prev_to_last_node.next != last_node:
            prev_to_last_node = prev_to_last_node.next
        
        prev_to_last_node.next = last_node.next
        self.tail = prev_to_last_node
        last_node.next = None
       
       
    ''' Return all the nodes of the list in order to be printed '''
    def __str__(self):
        if self.tail == None:
            return "Warning: List is empty"

        my_list = ""
        last_node = self.tail
        current = self.tail.next

        while True:
            my_list += f"{current.value} -> "
            if current == last_node:
                break
            current = current.next
        my_list += "None"
        
        return my_list    


if __name__ == '__main__':
    my_list = CircularLinkedList()
    # print(f"My list is Empty? {my_list.list_is_empty()}")
    # My list is Empty? True

    # Add new Node to the front of the list
    # my_list.add_to_front(Node(5))
    # my_list.add_to_front(Node(4))
    # my_list.add_to_front(Node(3))
    # my_list.add_to_front(Node(2))
    # my_list.add_to_front(Node(1))
    print(my_list)
    # 1 -> 2 -> 4 -> 5 -> None

    # Add new Node to the end of the list
    my_list.add_to_back(Node(1))
    my_list.add_to_back(Node(2))
    my_list.add_to_back(Node(3))
    my_list.add_to_back(Node(4))
    my_list.add_to_back(Node(5))
    print(my_list)
    # 1 -> 2 -> 3 -> 4 -> 5 -> None

    # my_list.remove_first()
    # print(my_list)
    # 2 -> 3 -> 4 -> 5 -> None

    # my_list.remove_last()
    # print(my_list)
    # # 1 -> 2 -> 3 -> 4 -> None
