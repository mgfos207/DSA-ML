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

    def get_height(self):
        left_height = self.left.height if self.left is not None else 0
        right_height = self.right.height if self.right is not None else 0
        return max(left_height, right_height)

    def get_left_right_height(self, type):
        return self.__getattribute__(type).height if self.__getattribute__(type) else 0

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

    def rotate_right(self):
        old_root = self
        new_root = self.left
        new_left = new_root.right
        old_root.left = new_left
        new_root.right = self
        new_root.height = 1 + new_root.get_height()
        return new_root

    def rotate_left(self):
        old_root = self
        new_root = self.right
        new_right = new_root.left
        old_root.right = new_right
        new_root.left = self
        new_root.right = self
        new_root.height = 1 + new_root.get_height()
        return new_root
        # self = new_root
        # self.height = 1 + self.get_height()

    def rebalance(self, val):
        """
        We should probably keep a temp variable to keep track of changes
        Once we complete making those changes then we should apply that temp variable
        As the new tree
        """
        new_root = self
        #Let's do a check of the tree to see if it needs rebalancing
        if self.bf > 1: #Left side is heavy rebalance
            #if val is greater than current left  node rotate left then right
            #else do the initial rebalnce which is the right rebalance
            if val > self.val:
                self.rotate('left', self.right)
                # self.right.rotate_left()
            # self.rotate_right()
            new_root = self.rotate('right')

        elif self.bf < -1: #Do the same thing except for the right
            #if val is greater than current right node right then left rotation
            #else do the left rotation
            if val > self.val:
                self.rotate('right', self.left)

            new_root = self.rotate('left')

        else:
            return new_root

        return new_root

    def insert_node(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = AVLTree(val)
                else:
                    #look left
                    self.left.insert_node(val)        
            else:
                if self.right is None:
                    self.right = AVLTree(val)
                else:
                    #look right
                    self.right.insert_node(val)
        else:
            self.val = AVLTree(val)

        left_height = self.get_left_right_height('left')
        right_height = self.get_left_right_height('right')
        self.bf = left_height - right_height
        self.height = 1 + self.get_height()
        new_root = self.rebalance(val)
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
    tree_obj = AVLTree(5)
    tree_obj = tree_obj.insert_node(3)
    tree_obj = tree_obj.insert_node(2)
    tree_obj.insert_node(10)

    tree_obj.find_val(2)

if __name__ == "__main__":
    main()