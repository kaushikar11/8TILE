import numpy as np

class Node:
    def __init__(self, s):
        self.child = s
        self.parent = None
        self.gn = 0
        self.hn = 0

    def get_fn(self):
        return self.gn + self.hn

    def update_gn(self, gn):
        self.gn = gn
        
    def update_hn(self, hn):
        self.hn = hn

    def update_parent(self, parent):
        self.parent = parent

    def get_current_state(self):
        return self.child
    
    def expand_node(fringe, explored_nodes, current_node, goal_node, zero, g, count):
        a = [list(item.get_current_state()) for item in explored_nodes]
        explored_nodes.append(current_node)
        current_node_array = np.asarray(current_node.get_current_state())

        directions = {
            'left': -1,
            'right': 1,
            'up': -3,
            'down': 3
        }

        for direction, move in directions.items():
            new_zero = zero + move
            if direction == 'left' and zero % 3 == 0:
                continue
            if direction == 'right' and zero % 3 == 2:
                continue
            if direction == 'up' and zero < 3:
                continue
            if direction == 'down' and zero >= 6:
                continue

            node_copy = current_node_array.copy()
            node_copy[zero], node_copy[new_zero] = node_copy[new_zero], node_copy[zero]
            distance = Distance.distance(node_copy, goal_node)
            count += 1
            
            if not list(node_copy) in a:
                node_copy_node = Node(node_copy)
                node_copy_node.update_gn(g)
                node_copy_node.update_hn(distance)
                node_copy_node.update_parent(current_node)
                fringe.append(node_copy_node)
        
        return count

class Puzzle:
    def least_fn(fringe):
        fn_fringe = [node.get_fn() for node in fringe]
        return fn_fringe.index(min(fn_fringe))

    def print_state(node):
        print("g(n) = ", node.get_gn(), " h(n) = ", node.get_hn(), " f(n) = ", node.get_fn() ,"\n")
        state = node.get_current_state()
        print(f"{state[0]} | {state[1]} | {state[2]}")
        print("---------")
        print(f"{state[3]} | {state[4]} | {state[5]}")
        print("---------")
        print(f"{state[6]} | {state[7]} | {state[8]}")
        print("----------------------------------------------------------\n")
        
    def goal_reached(explored_nodes, count):
        nodes_expanded = len(explored_nodes) - 1
        path = []
        init = explored_nodes[0]
        current = explored_nodes.pop()
        
        while init != current:
            path.append(current)
            current = current.get_parent()
        
        path.append(init)
        path.reverse()
        
        for i in path:
            Puzzle.print_state(i)
        
        print("Goal Reached \n")
        print("The number of nodes expanded: ", nodes_expanded, "\n")
        print("The number of nodes generated: ", count, "\n")
        print("Path Cost: ", len(path) - 1, "\n")

    def path(explored_nodes):
        explored_nodes.pop()

class Distance:
    @staticmethod
    def distance(arr, goal):
        distance = 0
        arr = np.asarray(arr).reshape(3, 3)
        goal = np.asarray(goal).reshape(3, 3)
        for i in range(8):
            a, b = np.where(arr == i + 1)
            x, y = np.where(goal == i + 1)
            distance += abs(a - x)[0] + abs(b - y)[0]
        return distance
