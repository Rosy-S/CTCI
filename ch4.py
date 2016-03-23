class BinaryTree:
    def __init__(self, content, leftchild=None, rightchild=None):
        self.content = content
        self.left = leftchild
        self.right = rightchild
        #-1 means the depth has not been calculated yet.
        self.depth = -1

    def __str__(self):
        return "( " + str(self.content) + " ( " + str(self.left) + " | " + str(self.right) + "))" 

    def insert(self, value):
    	new_tree = BinaryTree(value)
    	q = [self]
    	while True: 
    		node = q.pop(0)
    		if not node.left: 
    			node.left = new_tree
    			break
    		elif not node.right: 
    			node.right = new_tree
    			break
    		else: 
    			q.append(node.left)
    			q.append(node.right)
    	



import random
def make_random_balanced_tree(depth):
    if depth>0:
        tree = BinaryTree(random.randint(0, 100))
        tree.left=make_random_balanced_tree(depth-1)
        tree.right=make_random_balanced_tree(depth-1)
        return tree
    else:
        return None
class DirectedGraph: 
	def __init__(self, content): 
		self.content = content
		self.neighbours = []


#1) Given a directed graph, design an algorithim to find whether there is a path between two given nodes
def graph_path(node1, node2): 
	if node1 == node2: 
		return True
	elif node1 == None or node2 == None: 
		return False
	yet_to_explore_neighbours_queue = [node1]
	visited = set()
	while len(yet_to_explore_neighbours_queue) > 0: 
		node_to_explore = yet_to_explore_neighbours_queue.pop()
		print "exploring the node: ", node_to_explore.content
		for neigbor in node_to_explore.neighbours: 
			if neigbor == node2: 
				return True
			elif neigbor in visited: 
				continue
			else: 
				visited.add(neigbor)
				yet_to_explore_neighbours_queue.append(neigbor)
	return False

# n1 = DirectedGraph(1)
# n2 = DirectedGraph(2)
# n3 = DirectedGraph(3)
# n4 = DirectedGraph(4)
# n5 = DirectedGraph(5)
# n6 = DirectedGraph(6)

# n1.neighbours.append(n2)
# n2.neighbours.append(n3)
# n2.neighbours.append(n4)
# n4.neighbours.append(n5)
# n4.neighbours.append(n1)

# print graph_path(n1, n5)
# print "************************"
# print graph_path(n1, n6) 

#****************************************************************************************
#2) Given a sorted array with unique integer elements, write an algorithm to create
# a binary search tree with minimal height

def make_binary_tree(lst):
	if len(lst) == 0: 
		return
	if len(lst) == 1: 
		return BinaryTree(lst[0])
	midpoint = len(lst)//2 
	return BinaryTree(lst[midpoint], 
		make_binary_tree(lst[0:midpoint]), 
		make_binary_tree(lst[midpoint + 1:]))

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print make_binary_tree(lst)

#****************************************************************************************
#3) Is the given binary search tree balanced? 
def is_balanced(tree): 
	if tree == None:
		return True
	depths = []
	q = [(tree, 0)]
	while q: 
		current_tree, depth = q.pop()

		if not current_tree.left and not current_tree.right: 
			if depth not in depths: 
				depths.append(depth)

			if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1): 
				return False
		if current_tree.left: 
			q.append((current_tree.left, depth + 1))
		if current_tree.right: 
			q.append((current_tree.right, depth + 1))
	return True

#*********************************************************************
#4) print out linked lists of  the levels of a binary tree.
def bst_to_ll(tree): 
	list_of_values = []
	level_q = [tree]
	ll = []
	while level_q:
		new_q =[]
		for t in level_q: 
			ll.append(t.content)
			if t.left: 
				new_q.append(t.left)
			if t.right: 
				new_q.append(t.right)
		list_of_values.append(ll)
		level_q = new_q
		ll = []
	return list_of_values

balanced_tree = make_random_balanced_tree(3)
print balanced_tree
test = bst_to_ll(balanced_tree)
print test
		
#****************************************************************************************
#5) implement a function to see if a binary tree is a binary search tree
def is_bst(tree): 
	