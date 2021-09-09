import random
import numpy as np

class Node:

    def __init__(self, number):

        self.left_child = None
        self.right_child = None
        self.parent = None
        self.number = number


root = Node(1)

root.left_child = Node(2)
root.right_child = Node(5)

root.left_child.parent = root
root.right_child.parent = root

root.left_child.left_child = Node(3)
root.left_child.right_child = Node(4)

root.left_child.left_child.parent = root.left_child
root.left_child.right_child.parent = root.left_child

root.right_child.left_child = Node(6)
root.right_child.right_child = Node(7)

root.right_child.left_child.parent = root.right_child
root.right_child.right_child.parent = root.right_child

# root = Node(1)
#
# root.left_child = Node(2)
#
# root.left_child.parent = root
#
# root.left_child.left_child = Node(3)
#
# root.left_child.left_child.parent = root.left_child
#
# root.left_child.left_child.left_child = Node(4)
#
# root.left_child.left_child.left_child.parent = root.left_child.left_child

def get_num_node_dict(node):

    num_node_dict = {}

    def recurse(node, num_node_dict):
        if node is None:
            return

        recurse(node.left_child, num_node_dict)
        num_node_dict[node.number] = node
        recurse(node.right_child, num_node_dict)
        return

    recurse(node, num_node_dict)

    return num_node_dict


def traverse_upwards(node, step_size):

    visited = [node.number]

    step = 1

    while node.parent:

        node = node.parent

        if step % step_size == 0:

            visited.append(node.number)

        step += 1

    return visited


def beauty_calculator(A, B):

    num_node_dict = get_num_node_dict(root)
    painted_list = []

    for i in range(100000):
        rdm_A = random.randint(1, 4)
        rdm_B = random.randint(1, 4)
        list_A = traverse_upwards(num_node_dict[rdm_A], A)
        list_B = traverse_upwards(num_node_dict[rdm_B], B)
        painted_list.append(len(list(set(list_A+list_B))))

    return np.average(painted_list)


print(beauty_calculator(1, 1))


