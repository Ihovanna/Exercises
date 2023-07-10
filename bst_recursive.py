class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def helper(curr_node, value):
	
    # base case - reached a leaf
    if not curr_node:
        return None
    
    # base case - found what we are looking for
    elif value == curr_node.val:
        return curr_node.val
    
    # recursive case - key is less than current root's key
    elif value < curr_node.val:
        # call find on left subtree
        return helper(curr_node.left)
    
    # recursive case - key must be greater than current root's key
    # call find on right subtree
    return helper(curr_node.right)

def bst(arr):
    new_node = TreeNode(arr[len(arr)//2])
    print(f'new_node: {new_node.val}')
    root = new_node
    
    return helper(root, root.val)



arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]