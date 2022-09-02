class Node:
    def __init__(self, val):
        self.val = val
        self.next_val = None
        self.prev_val = None

    def add_node(self, Node):
        self.next_val = Node

    def get_val(self):
        return self.val

class SLinkedList:
    def __init__(self):
        self.head_val = None
        self.tail_node = None

    def add_head_val(self, Node):
        Node.next_val = self.head_val
        self.head_val = Node

    def add_link(self, Node):
        if self.tail_node is None: #First check if this is the first item after initial insert
            self.head_val.next_val = Node
            self.tail_node = self.head_val.next_val
        else:
            self.tail_node.next_val = Node
            self.tail_node = self.tail_node.next_val

    def add_tail_val(self, Node):
        if self.head_val is None:
            self.head_val = Node
        else:
            candiate_val = self.head_val
            while candiate_val:
                candiate_val = candiate_val.next_val
            
            candiate_val.next_Val = Node

    def find_node(self, val, Node=None):
        curr_node = None
        if Node is None: #Get the first val and compare otherwise recursive
            curr_node = self.head_val
            curr_val = self.head_val.get_val()
            if curr_val == val:
                return f"We've found the Node you were looking for {val}"
        else:
            curr_node = Node
            curr_val = curr_node.get_val()
            if curr_val == val:
                return f"We've found the Node you were looking for {val}"
        
        next_node = curr_node.next_val
        if next_node is None:
            return f"Sorry we can't find the Node you were looking for {val}"
        else:
            return self.find_node(val, next_node)

    def print_linked_list(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.get_val())
            print_val = print_val.next_val


class DLinkedList:
    def __init__(self):
        self.head_val = None
        self.tail_node = None

    def add_head_val(self, Node):
        Node.next_val = self.head_val
        self.head_val = Node

    def add_link(self, Node):
        if self.tail_node is None: #First check if this is the first item after initial insert
            self.head_val.next_val = Node
            self.tail_node = self.head_val.next_val
        else:
            Node.prev_val = self.tail_node
            self.tail_node.next_val = Node
            self.tail_node = self.tail_node.next_val

    def add_tail_val(self, Node):
        if self.head_val is None:
            self.head_val = Node
        else:
            candiate_val = self.head_val
            while candiate_val:
                candiate_val = candiate_val.next_val
            
            candiate_val.next_Val = Node

    def find_node(self, val, Node=None):
        curr_node = None
        if Node is None: #Get the first val and compare otherwise recursive
            curr_node = self.head_val
            curr_val = self.head_val.get_val()
            if curr_val == val:
                return f"We've found the Node you were looking for {val}"
        else:
            curr_node = Node
            curr_val = curr_node.get_val()
            if curr_val == val:
                return f"We've found the Node you were looking for {val}"
        
        next_node = curr_node.next_val
        if next_node is None:
            return f"Sorry we can't find the Node you were looking for {val}"
        else:
            return self.find_node(val, next_node)

    def print_linked_list(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.get_val())
            print_val = print_val.next_val

def main():
    node_1 = Node(20)
    node_2 = Node(23)
    node_3 = Node(5456)
    node_4 = Node(323482093)
    node_5 = Node(2892714455)
    node_6 = Node(714455)
    node_7 = Node(255)
    node_8 = Node(84849817)
    ll_obj = SLinkedList()
    ll_obj.add_head_val(node_1)
    ll_obj.add_link(node_2)
    ll_obj.add_link(node_3)
    ll_obj.add_link(node_4)
    ll_obj.add_link(node_5)
    ll_obj.add_link(node_6)
    ll_obj.add_link(node_8)
    ll_obj.add_link(node_7)
    answ = ll_obj.find_node(21)
    print(answ)
    ll_obj = DLinkedList()
    ll_obj.add_head_val(node_1)
    ll_obj.add_link(node_2)
    ll_obj.add_link(node_3)
    ll_obj.add_link(node_4)
    ll_obj.add_link(node_5)
    ll_obj.add_link(node_6)
    ll_obj.add_link(node_8)
    ll_obj.add_link(node_7)
    ll_obj.print_linked_list()

if __name__ == "__main__":
    main()
