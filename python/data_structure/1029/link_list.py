class Node:
    def __init__(self):
        self.data = ""
        self.next = None

class Link_list:
    def __init__(self):
        self.head = None
    
    def add_front(self,data):
        new_node = Node()
        new_node.data = data
        new_node.next = self.head
        self.head = new_node
    # def add_between(self):
    def add_end(self,data):
        new_node = Node()
        new_node.data = data
        if self.head == None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def print_link(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

List = Link_list()

List.add_front(1234)
List.add_front(5678)
List.add_end("ABCD")

List.print_link()