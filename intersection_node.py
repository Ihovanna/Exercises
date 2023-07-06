class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(a, b):

    head_1 = a
    head_2 = b

    # if not a or not b:
    #     raise TypeError('List is empty')

    while head_1 is not None:
        print(f'head_1: {head_1.val}')

        while head_2 is not None:
            # print(f'head_2: {head_2.val}')
                
            if head_1 == head_2:
                print(f'returned head.val: {head_1.val}')
                return head_1

            head_2 = head_2.next
        
        head_2 = b
        head_1 = head_1.next

    return None

### ^^This code assumes that lists are of same length and will intersect at same index! ###
# --> need to implement code where lists of different lengths can compare all nodes of one
#       list against all nodes of the other!


# Arrange
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")

node_x = Node("X")
node_y = Node("Y")
node_z = Node("Z")

node_one = Node("1")
node_two = Node("2")
node_three = Node("3")
node_one.next = node_two
node_two.next = node_three

# List A: ["D", "E", "F", "1", "2", "3"]
node_d.next = node_e
node_e.next = node_f
node_f.next = node_one

# List B: ["X", "Y", "Z", "1", "2", "3"]
node_x.next = node_y
node_y.next = node_z
node_z.next = node_one

head_a = node_d
head_b = node_x
head_c = []

# Act
print(intersection_node(head_a, head_c))

# asserting: node_one