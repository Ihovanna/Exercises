'''
arr = sorted array of integers

Write a function to create a balanced Binary Search Tree from the contents of the array. 
Return the root of the binary search tree. 

- no duplicate elements in the array
- not required to implement self-balancing
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def arr_to_bst(arr):
    root = None
    new_node = TreeNode(arr[len(arr)//2])
    pop_list = []

    if not root:
        root = new_node

    curr_node = root

    while arr:
        mid = len(arr)//2
        popped = arr.pop(mid)
        pop_list.append(popped)
        print(curr_node.val)

        if len(pop_list) >= 2:
            new_node = TreeNode(pop_list[len(pop_list) - 1])
            if new_node.val < curr_node.val:
                if not curr_node.left:
                    curr_node.left = new_node
                elif curr_node.left:
                    curr_node = curr_node.left
                    print(f'traversed LEFT - curr_node: {curr_node.val}')
            else:
                if not curr_node.right:
                    curr_node.right = new_node
                elif curr_node.right:
                    curr_node = curr_node.right
                    print(f'traversed RIGHT - curr_node: {curr_node.val}')
                    



# Test Case #1
# height = 4
arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]
# tree = TreeNode(25, TreeNode())

arr_to_bst(arr)