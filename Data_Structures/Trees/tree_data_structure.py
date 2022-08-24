class Tree:
    def __init__(self, val):
        self.val = None
        if val is not None:
            self.val = val

        self.left = None
        self.right = None
    
    def insert_node(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = Tree(val)
                else:
                    #look left
                    self.left.insert_node(val)        
            else:
                if self.right is None:
                    self.right = Tree(val)
                else:
                #look right
                    self.right.insert_node(val)
        else:
            self.val = Tree(val)

    def find_val(self, val):
        '''
        How can you find the value in BST (Binary search Tree - it's in order)
        We can start with the value and do a check to see if it equals the root
        We can then do a check to see if the val is less than the root search left
        Otherwise go right and do the same process
        This can be done recursively with base statements to say if val == current node val
        Another base case is if the current node doesn't have any appropriate node to traverse next return false
        Let's do this
        '''
        #Base case
        if self.val == val:
            print("Found it :)")
            return True
        elif self.val > val:
            #Go left
            if self.left is None:
                print("Negative")
                return False
            else:
                self.left.find_val(val)
        else:
            #Go right
            if self.right is None:
                print("Negative")
                return False
            else:
                self.right.find_val(val)

    def print_tree(self):
        if self.left is not None:
            self.left.print_tree()
        print(self.val)
        if self.right is not None:
            self.right.print_tree()


def main():
    tree_obj = Tree(10)
    tree_obj.left = Tree(5)
    tree_obj.right = Tree(13)
    tree_obj.insert_node(12)
    tree_obj.insert_node(3)
    tree_obj.insert_node(16)

    tree_obj.find_val(2)

if __name__ == "__main__":
    main()