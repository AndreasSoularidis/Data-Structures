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
    def list_is_empty(self):
        return not self.head


    # Add a new node to the front of the linked list
    def add_to_front(self, new_node):
        if self.list_is_empty():
           self.head = new_node
        else:
            # Step 2: Link head with the new node
            new_node.next = self.head
            self.head = new_node


    # Add a new node at the end of the linked list
    def add_to_back(self, new_node):
        if self.list_is_empty():
            self.head = new_node
        else:
            # Step 2: Find the last element of the lined list
            last = self.head
            while last.next != None:
                last = last.next
            # Step 3: Link the last node with the new node
            last.next = new_node
    

    # Add a new node before a particular node
    def add_before_node(self, target_node, new_node):
        target = self.head
        prev_node = None
        # Step 2: Find previous node
        while target.value != target_node:
            prev_node = target
            target = target.next
        # Step 3: Link new node with target node
        new_node.next = prev_node.next
        # Step 4: Link previous node with new node
        prev_node.next = new_node


    # Add a new node after a particular node
    def add_after_node(self, target, new_node):
        target_node = self.head
        # Step 2: Find the target node
        while target_node.value != target:
            target_node = target_node.next

        # Step 3: Link the new node with the next of target node
        new_node.next = target_node.next
        # Step 4: Link the target node with the new node
        target_node.next = new_node


    # Return the first node of the linked list
    def return_first(self):
        if self.list_is_empty():
            print("Error: List is empty")
            return 
        return self.head.value


    # Return the last node of the linked list
    def return_last(self):
        if self.list_is_empty():
            print("Error: List is empty")
            return 
        # Traverse all the nodes till the end of the linked list
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        # Return the last node
        return last_node.value


    # Remove the first node of the linked list
    def remove_first(self):
        if self.list_is_empty():
            print("Error: List is empty")
            return

        self.head = self.head.next


    # Remove the last node of the linked list
    def remove_last(self):
        if self.list_is_empty():
            print("Error: List is empty")
            return
        # Find the last and the second to last nodes
        last_node = self.head
        prev_node = None
        while last_node.next != None:
            prev_node = last_node
            last_node = last_node.next
        # Change the connection of second to last node to None
        prev_node.next = None


    # Remova a node based on a key
    def remove_key(self, key):
        if self.list_is_empty():
            print("Error: List is empty")
            return
        # Search that node (target_node) and the previous node
        target_node = self.head
        prev_node = None
        while target_node != None :
            if target_node.value == key:
                # Previous node connects with the node with which target node is connected
                prev_node.next = target_node.next
                break
            prev_node = target_node
            target_node = target_node.next
        else:
            print(f"The key {key} doesn't exist in the list")

    
    # Check if the key exists in the list
    def key_in_list(self, key):
        if self.list_is_empty():
           print("Error: List is empty")
           return
        # Traverse all the nodes of the list
        target_node = self.head
        while target_node != None:
            if target_node.value == key:
                print(f"The key {key} exists in the list")
                break
            target_node = target_node.next
        else:
            print(f"The key {key} doesn't exist in the list")


    def __str__(self):
        list = ""
        # current is the first node of the linked list
        current = self.head 
    
        while current != None:
            list += f"{current.value} -> " 
            current = current.next
        list += "None" 
        return list


if __name__ == '__main__':
    my_linked_list = LinkedList()
    # my_linked_list.add_to_front(Node(1))
    # my_linked_list.add_to_front(Node(2))
    # my_linked_list.add_to_front(Node(3))
    # my_linked_list.add_to_front(Node(4))
    # my_linked_list.add_to_front(Node(5))

    my_linked_list.add_to_back(Node(1))
    my_linked_list.add_to_back(Node(2))
    my_linked_list.add_to_back(Node(3))
    my_linked_list.add_to_back(Node(4))
    my_linked_list.add_to_back(Node(5))
    
    print(my_linked_list)

    # my_linked_list.add_before_node(4, Node(10))
    # print(my_linked_list)
    # my_linked_list.add_after_node(2, Node(4))
    # print(my_linked_list)

    # print(f"First Node: {my_linked_list.return_first()}")
    # print(f"Last Node: {my_linked_list.return_last()}")

    # my_linked_list.remove_first()
    # print(my_linked_list)
    # my_linked_list.remove_last()
    # print(my_linked_list)
    # my_linked_list.remove_key(3)
    # print(my_linked_list)

    # my_linked_list.key_in_list(4)
    # my_linked_list.key_in_list(6)
        