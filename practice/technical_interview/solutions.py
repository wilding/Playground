# ////////////////////////////  Question 1  ////////////////////////////


def question1(s, t):
    """input- two strings
    output- True if anagram of t is substring in s,
    False otherwise"""
    if not t:
        return False
    t_list = list(t)
    for i in range(len(s)):
        value = s[i]
        if value in t_list:
            for j in range(len(t_list)):
                if t_list[j] == value:
                    del t_list[j]
                    break
        else:
            t_list = list(t)
        if not t_list:
            return True
    return False


print 'test for question1():\n'
print question1("Udacity", "ad")
# should be True
print question1("Udacity", "Udacity")
# should be True
print question1("Udacity", "cd")
# should be False
print question1("Udacityudacity", "ad")
# should be True
print question1("Dudacity", "ad")
# should be True
print question1("Udacity", "")
# should be False
print '\n'


# ////////////////////////////  Question 2  ////////////////////////////


def question2(a):
    """input- string
    output- longest palindrom contained in string"""
    a_mod = a.translate(None, ' .,;"?[]/!@#$%^&*()-_=+:<>')
    a_length = len(a_mod)
    while a_length > 1:
        start = 0
        end = a_length
        while end <= len(a_mod):
            substring = a_mod[start:end]
            if substring == substring[::-1]:
                return substring
            start += 1
            end += 1
        a_length -= 1


print 'Test for question2():\n'
string1 = "racecar"
string2 = "noon"
string3 = "enoracecar"
string4 = "nopalindrome"
string5 = "a man, a plan, a canal: panama"
print question2(string1)
# should be 'racecar'
print question2(string2)
# should be 'noon'
print question2(string3)
# should be 'racecar'
print question2(string4)
# should be None
print question2(string5)
# should be 'amanaplanacanalpanama'
print '\n'


# ////////////////////////////  Question 3  ////////////////////////////


def question3(adjacency_dict):
    """input - adjacency dict of an undirected graph
    output- adjacency dict of minimum spanning tree
    adjacency dict format:
    {'A': [('B', 2)],
    'B': [('A', 2), ('C', 5)],
    'C': [('B', 5)]}"""
    return minspantree_helper(adjacency_dict, adjacency_dict.keys()[0], [], {})


def minspantree_helper(matrix, start_node, priority_queue, final_tree):
    """recursive helper function for question3()
    inputs: adjacency dictionary, value of start node, priority queue, and final adjacency dict
    output: final adjacency dict"""
    # iterate through edges of start node
    for tup in matrix[start_node]:
        # if edge destination is already in final tree, don't add it to priority queue
        # if edge destination is not in final tree, add edge to priority queue
        if final_tree and tup[0] in final_tree.keys():
            continue
        elif not priority_queue:
            priority_queue.append((start_node, tup[0], tup[1]))
        else:
            i = 0
            while i < len(priority_queue) and priority_queue[i][2] > tup[1]:
                i += 1
            priority_queue.insert(i, (start_node, tup[0], tup[1]))
    # remove minimum edge from priority queue
    min_edge = priority_queue.pop()
    # add edge to final tree
    if start_node not in final_tree:
        final_tree[min_edge[0]] = [(min_edge[1], min_edge[2])]
        final_tree[min_edge[1]] = [(min_edge[0], min_edge[2])]
    else:
        final_tree[min_edge[0]].append((min_edge[1], min_edge[2]))
        final_tree[min_edge[1]] = [(min_edge[0], min_edge[2])]
    # remove edges from priority queue which travel to nodes already in the tree
    counter = 0
    while counter < len(priority_queue):
        if priority_queue[counter][1] in final_tree.keys():
            del priority_queue[counter]
        else:
            counter += 1
    # return final tree if finished
    if len(matrix) == len(final_tree):
        return final_tree
    # if not, continue recursively with new edge's destination as the start node
    else:
        return minspantree_helper(matrix, min_edge[1], priority_queue, final_tree)


print 'test for question3():\n'
test_matrix = {'A': [('B', 2), ('C', 8)], 'B': [('A', 2), ('C', 5)],'C': [('B', 5), ('A', 8)]}
test_matrix2 = {
    'A': [('F', 5), ('B', 2), ('E', 14), ('C', 8), ('D', 10)],
    'B': [('F', 8), ('A', 2), ('C', 5), ('E', 8)],
    'C': [('D', 11), ('A', 8), ('F', 12), ('B', 5), ('E', 7)],
    'D': [('A', 10), ('F', 20), ('E', 30), ('C', 11)],
    'E': [('C', 7), ('D', 30), ('A', 14), ('B', 8)],
    'F': [('A', 5), ('D', 20), ('C', 12), ('B', 8)]}
print question3(test_matrix)
# should be {'A': [('B', 2)], 'C': [('B', 5)], 'B': [('A', 2), ('C', 5)]}
print '\n'
print question3(test_matrix2)
# should be {'A': [('B', 2), ('F', 5), ('D', 10)], 'C': [('B', 5), ('E', 7)], 'B': [('A', 2), ('C', 5)], 'E': [('C', 7)], 'D': [('A', 10)], 'F': [('A', 5)]}
print '\n'


# ////////////////////////////  Question 4  ////////////////////////////


def question4(tree_matrix, root, node1, node2):
    """inputs - tree represented by matrix where index is the integer stored in the node and 1 = child node
    non-negative int representing root
    2 non-negative ints representing nodes
    output- non-negative int representing least common ancestor of node1 and node2
    Both nodes can be assumed to be in the tree and the tree can be assumed to follow BST rules."""
    ancestors1 = get_ancestors(tree_matrix, root, node1)
    ancestors2 = get_ancestors(tree_matrix, root, node2)
    for ancestor in ancestors1:
        if ancestor in ancestors2:
            return ancestor


def get_ancestors(tree_matrix, root, node):
    """helper function for question4().
    inputs- tree matrix, int representing root node, and int representing node
    output- list of given node and all its ancestors up to the root"""
    ancestors = [node]
    current = node
    while current != root:
        for i in range(len(tree_matrix)):
            if tree_matrix[i][current] == 1:
                ancestors.append(i)
                current = i
                break
    return ancestors


print 'test for question4():\n'
test_tree = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print question4(test_tree, 7, 0, 2)
# should be 1
print question4(test_tree, 7, 0, 5)
# should be 3
print question4(test_tree, 7, 2, 9)
# should be 7
print question4(test_tree, 7, 7, 14)
# should be 7
print question4(test_tree, 7, 1, 2)
# should be 1
print '\n'


# ////////////////////////////  Question 5  ////////////////////////////


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def question5(ll, m):
    """inputs- first node of linked list, int
    output- node that is m nodes from the end of the list"""
    current = ll
    downstream = current
    for i in range(m):
        downstream = downstream.next
        if not downstream:
            if i == m - 1:
                return current.data
            else:
                return None
    while downstream.next:
        current = current.next
        downstream = downstream.next
    if current.next:
        return current.next.data
    else:
        return None


print 'test for question5():\n'
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print question5(n1, 0)
# should be None
print question5(n1, 1)
# should be 5
print question5(n1, 2)
# should be 4
print question5(n1, 3)
# should be 3
print question5(n1, 4)
# should be 2
print question5(n1, 5)
# should be 1
print question5(n1, 6)
# should be None
print '\n'
