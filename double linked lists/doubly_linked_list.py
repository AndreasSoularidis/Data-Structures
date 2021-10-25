''' Node class represents a node of the list'''
from typing import Counter


class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None



''' LinkedList class represents the doubly linked list'''
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    '''Returns True if the list is empty (so self.head = None) 
    Otherwise, returns False'''
    def list_is_empty(self):
        return not self.head
    
    
    ''' Add a new node to the front of the doubly linked list '''
    def add_to_front(self, new_node):
        if self.list_is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
    
    
    ''' Add a new Node at the end of the doubly linked list '''
    def add_to_back(self, new_node):
        if self.list_is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            

    ''' Add a new Node before a particular Node'''
    def add_before_node(self, target_value, new_node):
        target = self.head
        previous_node = None
        
        # Step 2: Find previous None
        while target.value != target_value:
            previous_node = target
            target = target.next

        # Step 3: Link the new Node with the target Node
        new_node.next = previous_node.next
        previous_node.next.previous = new_node
        # Step 4: Link previous Node with new Node
        previous_node.next = new_node
        new_node.previous = previous_node

    
    ''' Remove the first Node of the doubly linked list'''
    def remove_first(self):
        if self.list_is_empty():
            print("Warning: List is empty")
            return

        # Check if the list contains exactly one Node or not
        if self.head.next == None: # One Node
            # Step 1: Update the head to None
            self.head = None
            # Step 2: Update the tail to None
            self.tail = None
        else: # More than one Nondes
            # Step 1: Link the head with the second node. So previous second None is now first
            self.head = self.head.next
            # Step 2: Update the previous pointer of the first Node to None
            self.head.previous = None
    

    ''' Remove the last Node of the doubly linked list'''
    def remove_last(self):
        if self.list_is_empty():
            print("Warning: List is empty")
            return

        # Check if the list contains exactly one Node or not
        if self.head.next == None: # One Node
            # Step 1: Update the head to None
            self.head = None
            # Step 2: Update the tail to None
            self.tail = None
        else: # More than one Nondes
            # Step 1: Find the second to last Node
            second_to_last_node = self.tail.previous
            # Step 2: Change the connection to None
            second_to_last_node.next = None
            # Step 3: Change the previous pointer of the last Node to None
            self.tail.previous = None
            # Step 4: Change the tail pointer to second to last node
            self.tail = second_to_last_node


    ''' Remove a node based on a particular key'''
    def remove_key(self, key):
        if self.list_is_empty():
            print("Warning: List is empty")
            return

        # Step 1: Find the target Node
        target_node = self.head
        while target_node is not None and target_node.value != key:
            target_node = target_node.next
        
        if target_node is None:
            print(f"Warning: {key} does not exist in the list")
            return
        
        previous_node = target_node.previous

        # Step 2: If the target is the last Node update the tail
        if target_node.next is None:
            self.tail = previous_node

        # Step 3: If the target Node is the first Node of the list
        if previous_node is None:
            self.head = target_node.next
            if self.head is not None:
                self.head.previous = None
            return
        # Step 4: Change the connection of the previous Node to the None after the target Node
        previous_node.next = target_node.next
        # Step 5: Change the previous pointer of the target Node to None
        target_node.previous = None
        

    ''' Traverse a doubly linked list with a tail from end to start'''
    def traverse_backwards(self):
        current = self.tail

        while current is not None:
            print(f"{current.value} -> ", end="")
            current = current.previous
        print("None")



    ''' Return all the nodes of the list in order to be printed '''
    def __str__(self):
        my_list = ""
        current = self.head

        while current != None:
            my_list += f"{current.value} -> "
            current = current.next
        my_list += "None"
        
        return my_list    
    


if __name__ == '__main__':
    my_list = DoublyLinkedList()
    print(f"My list is Empty? {my_list.list_is_empty()}")
    # My list is Empty? True

    # Add new Node to the front of the list
    my_list.add_to_front(Node(5))
    my_list.add_to_front(Node(4))
    my_list.add_to_front(Node(3))
    my_list.add_to_front(Node(2))
    my_list.add_to_front(Node(1))
    print(my_list)
    # 1 -> 2 -> 4 -> 5 -> None

    # Add new Node to the end of the list
    # my_list.add_to_back(Node(1))
    # my_list.add_to_back(Node(2))
    # my_list.add_to_back(Node(4))
    # my_list.add_to_back(Node(5))
    # print(my_list)
    # # 1 -> 2 -> 4 -> 5 -> None

    # my_list.add_before_node(4, Node(3))
    # print(my_list)
    # # 1 -> 2 -> 3 -> 4 -> 5 -> None

    # my_list.remove_first()
    # print(my_list)
    # 2 -> 3 -> 4 -> 5 -> None 

    # my_list.remove_last()
    # print(my_list)
    # # 1 -> 2 -> 3 -> 4 -> None

    # my_list.remove_key(6)
    # print(my_list)
    # # Warning: 6 does not exist in the list
    
    # my_list.remove_key(3)
    # print(my_list)
    # # 1 -> 2 -> 4 -> 5 -> None

    # my_list.remove_key(1)
    # print(f"{my_list} head value: {my_list.head.value} tail value: {my_list.tail.value}")
    # # 2 -> 4 -> 5 -> None head value: 2 tail value: 5

    # my_list.remove_key(5)
    # print(f"{my_list} head value: {my_list.head.value} tail value: {my_list.tail.value}")
    # # 2 -> 4 -> None head value: 2 tail value: 4
    # my_list.remove_key(2)
    # print(f"{my_list} head value: {my_list.head.value} tail value: {my_list.tail.value}")
    # # 4 -> None head value: 4 tail value: 4

    # print("Traverse Backwards")
    # my_list.traverse_backwards()