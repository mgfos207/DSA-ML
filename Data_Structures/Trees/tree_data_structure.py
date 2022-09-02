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
        print(info)

class AVLTree(BinarySearchTree):
    def __init__(self, val):
        super().__init__(val)
        self.height = 1
        self.bf = 0

    def get_height(self, Node):
        if Node is None:
            return 0
        return Node.height

    def rotate(self, rot_dir, node=None):
        #check to see if the node exists with data otherwise assign to the None branch
        new_root = None
        if node is not None:
            new_root = getattr(self.__getattribute__(node), f"rotate_{rot_dir}")()
        else:
            old_root = self
            if rot_dir == 'right':
                new_root = self.left
                new_root.right = old_root
            else:
                new_root = self.right
                new_root.left = old_root

        return new_root

    def update_tree(self, new_root):
        self = new_root

    def rotate_right(self, Node):
        new_root = Node.left
        old_right = new_root.right
        new_root.right = Node
        Node.left = old_right
        Node.height = 1 + max(self.get_height(Node.left), self.get_height(Node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def rotate_left(self, Node):
        new_root = Node.right
        old_right = new_root.left
        new_root.left = Node
        Node.right = old_right
        Node.height = 1 + max(self.get_height(Node.left), self.get_height(Node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def rebalance(self,val, bf, Node):
        """
        We should probably keep a temp variable to keep track of changes
        Once we complete making those changes then we should apply that temp variable
        As the new tree
        """
        new_root = Node
        #Let's do a check of the tree to see if it needs rebalancing
        if bf > 1: #Left side is heavy rebalance
            #if val is greater than current left  node rotate left then right
            #else do the initial rebalnce which is the right rebalance
            if val > new_root.left.val:
                new_root.left = self.rotate_left(new_root.left)

            new_root = self.rotate_right(new_root)

        elif bf < -1: #Do the same thing except for the right
            #if val is greater than current right node right then left rotation
            #else do the left rotation
            if val < new_root.rightval:
                new_root.right = self.rotate_right(new_root.right)

            new_root = self.rotate_left(new_root)

        else:
            return new_root

        return new_root

    def insert_node(self, val, root):
        if root.val is not None:
            if val < root.val:
                if root.left is None:
                    root.left = AVLTree(val)
                else:
                    #look left
                    root.left = self.insert_node(val, root.left)        
            else:
                if root.right is None:
                    root.right = AVLTree(val)
                else:
                    #look right
                    root.right = self.insert_node(val, root.right)
        else:
            root.val = AVLTree(val)

        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        root.height = 1 + max(left_height, right_height)
        new_root = root
        bf = left_height - right_height
        if bf > 1 or bf < -1:
            return self.rebalance(val, bf, root)

        return new_root


def main():
    #Binary Search Tree
    tree_obj = BinarySearchTree(10)
    tree_obj.left = BinarySearchTree(5)
    tree_obj.right = BinarySearchTree(13)
    tree_obj.insert_node(12)
    tree_obj.insert_node(3)
    tree_obj.insert_node(16)

    tree_obj.find_val(2)

    #AVL Tree
    tree_obj = AVLTree(10)
    tree_obj = tree_obj.insert_node(2, tree_obj)
    tree_obj = tree_obj.insert_node(3, tree_obj)

    tree_obj.insert_node(40)

    # tree_obj.find_val(2)

if __name__ == "__main__":
    main()