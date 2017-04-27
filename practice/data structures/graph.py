class Node(object):
    """docstring for Node"""
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    """docstring for Edge"""
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    """docstring for Graph"""
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_value):
        """Creates a new node with the given value and
        inserts it into the graph's list of nodes"""
        new_node = Node(new_node_value)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_value, node_from_val, node_to_val):
        """Creates a new edge with a given value between nodes with the specified values.
        If no nodes exist with the given values, new nodes are created.
        The new edge is then added to the graph's list of edges,
        as well as the individual node's list of edges"""
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
        if from_found is None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
        if to_found is None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_value, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Returns a list of tuples, each representing an edge,
        that contain the edge value, the value of the origin node,
        and the value of the destination node"""
        edge_list = []
        for edge in self.edges:
            edge_list.append((edge.value, edge.node_from.value, edge.node_to.value))
        return edge_list

    def get_adjacency_list(self):
        """Returns a list of lists, list indices
        represent each node in the graph.
        Each sublist contains tuples
        for each outbound edge from the node.
        The tuples store the value of the connected node,
        and the value of the edge."""
        adjacency_list = []
        for node in self.nodes:
            sublist = []
            for edge in node.edges:
                if edge.node_to != node:
                    sublist.append((edge.node_to.value, edge.value))
            if sublist:
                adjacency_list.append(sublist)
            else:
                adjacency_list.append(None)
        return adjacency_list

    def get_adjacenty_matrix(self):
        """Returns a list of lists, forming a matrix
        where the row represents the origin node and
        the column represents the destination node.
        If an edge exists between the origin and the destination,
        it's value is added to the appropriate position within the matrix"""
        adjacency_matrix = []
        for node in self.nodes:
            matrix_row = []
            counter = 1
            for subnode in self.nodes:
                for edge in node.edges:
                    if edge.node_to == subnode and edge.node_from == node:
                        matrix_row.append(edge.value)
                if len(matrix_row) < counter:
                    matrix_row.append(0)
                counter += 1
            adjacency_matrix.append(matrix_row)
        return adjacency_matrix

    def dfs(self, start_node_num):
        """Outputs a list of numbers corresponding to the traversed nodes
        in a Depth First Search.
        ARGUMENTS: start_node_num is the starting node number (integer)
        RETURN: a list of the node values (integers)."""
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node, visited=[])

    def bfs(self, start_node_num):
        """TODO: Create an iterative implementation of Breadth First Search
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes.
        ARGUMENTS: start_node_num is the node number (integer)
        RETURN: a list of the node values (integers)."""
        ret_list = [start_node_num]
        for node_value in ret_list:
            node = self.find_node(node_value)
            for edge in node.edges:
                if edge.node_from == node and edge.node_to.value not in ret_list:
                    ret_list.append(edge.node_to.value)
        return ret_list

    def dfs_helper(self, start_node, visited):
        """TODO: Write the helper function for a recursive implementation
        of Depth First Search iterating through a node's edges. The
        output should be a list of numbers corresponding to the
        values of the traversed nodes.
        ARGUMENTS: start_node is the starting Node
        Because this is recursive, we pass in the set of visited node
        values.
        RETURN: a list of the traversed node values (integers).
        """
        if start_node:
            visited.append(start_node.value)
            for edge in start_node.edges:
                if edge.node_from == start_node and edge.node_to.value not in visited:
                    visited = self.dfs_helper(edge.node_to, visited)
        return visited

    def find_node(self, node_value):
        """input: value
        output: first node in the graph with given value"""
        for node in self.nodes:
            if node_value == node.value:
                return node
        return None
