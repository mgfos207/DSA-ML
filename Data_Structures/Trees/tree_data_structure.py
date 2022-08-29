class BinarySearchTree:
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
                    self.left = BinarySearchTree(val)
                else:
                    #look left
                    self.left.insert_node(val)        
            else:
                if self.right is None:
                    self.right = BinarySearchTree(val)
                else:
                #look right
                    self.right.insert_node(val)
        else:
            self.val = BinarySearchTree(val)

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

    def info_queue(self):
        info = """
        Binary Search trees (BST) are a special type of binary tree where the left child node  always has a value less than the parent, and the right is greater than the parent.
        The following operations can be done with their repsective Time Complexity:
        Searching - O(n), but on average it will be more like O(h), where h is the height of the tree
        Insertion - O(n), but in general it will be more like O(h), where h is the height of the tree
        Deletion - O(n), but in general it will be more like O(h), where h is the height of the tree
        
        The following are what makes a tree classified as a Binary Tree
        1. The left subtree of a node contains only nodes with keys lesser than the node's key
        2. The right subtree of a node contains only nodes with keys greater tthan the node's key
        3. The left and right subtree must also be a binary search tree
        """

def main():
    tree_obj = BinarySearchTree(10)
    tree_obj.left = BinarySearchTree(5)
    tree_obj.right = BinarySearchTree(13)
    tree_obj.insert_node(12)
    tree_obj.insert_node(3)
    tree_obj.insert_node(16)

    tree_obj.find_val(2)

if __name__ == "__main__":
    main()