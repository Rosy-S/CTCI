def find_largest(grid, n): 
	memo = [None] * (n * n)
	count = 0
	for i in range(n): 
		for j in range(n): 
			q = []
			if j == n - 1: 
				continue
			else: 
				if grid[i][j + 1] - grid[i][j] == 1: 





class Stack:
	 def __init__(self):
		 self.items = []

	 def isEmpty(self):
		 return self.items == []

	 def push(self, item):
		 self.items.append(item)

	 def pop(self):
		 return self.items.pop()

	 def peek(self):
		 return self.items[len(self.items)-1]

	 def size(self):
		 return len(self.items)

# reverse a string using a stack
def revstring(str): 
	result_str = Stack()
	str_lst = list(str)
	while str_lst: 
		result_str.push(str_lst.pop())
		print result_str
	return result_str

#Chapter 1##########################################################################

# implement an algorithm to determine if a string has all unique characters.
def is_unique (string): 
	string.lower()
	for i, l in enumerate(string): 
		if l in string[(i + 1):]: 
			return False
	return True 

# Given two strings, write a method to decide if one is a permutation of the other.
def is_perm (str1, str2):
	pass

# implement a method to perform basic string compression using counts of repeted characters
# ex: 'aabccccaaa' would become 'a2b1c4a3'
def string_compression(string): 
	index = 0
	counter = 1
	results = []
	while index < (len(string) - 1): 
		if string[index] != string[index +1]: 
			results.append(string[index] + str(counter))
			counter = 1
			index += 1
		else: 
			counter += 1
			index += 1
	print "the result list ", results
	results = ''.join(results)
	return results

#Chapter 2#################################################################
class Node(object): 
	def __init__(self, data): 
		self.data = data
		self.next = None

	def getData(self): 
		return self.data

	def getNext(self): 
		return self.next

	def setNext(self, node):
		if not isinstance(node, Node): 
			node = Node(node)
		self.next = node

	def setData(self, data): 
		self.data = data

	def __str__(self): 
		return "Node Object <data = %s next = %s>" % (self.data, self.next)

class LL(object): 
	def __init__(self): 
		self.head = None
		self.tail = None


	def __str__(self):
		if self.head != None:
			index = self.head
			nodestore = [str(index.data)]
			while index.next != None:
				index = index.next
				nodestore.append(str(index.data))
			return "LinkedList  [ " + "->".join(nodestore) + " ]"
		return "LinkedList  []"

	def addNode(self, value): 
		node = Node(value)
		if self.head == None: 
			self.head = node 
			self.tail = node
		else: 
			self.tail.next = node
			self.tail = node 

	def removeNode(self, value): 
		current = self.head
		previous = None

		while current is not None: 
			if current.data == value: 
				if previous is None:  
					self.head = current.next
				else: 
					previous.next = current.next
				break
			previous = current
			current = current.next 

	def removeMiddle(self, c): 
		current = self.head
		previous = None

		while current.next is not None: 
			if current.data == c: 
				print "IM in this loop"
				previous.next = current.next
				current = current.next.next
			else: 
				print "I'm in the else"
				previous = current
				current = current.next

	# def removeDupes(self): 
	# 	dupe_dict = {}
	# 	current = self.head
	# 	previous = None
	# 	while current is not None: 
	# 		print dupe_dict
	# 		if current.data in dupe_dict: 
	# 			self.removeNode(current.data)
	# 		else: 
	# 			dupe_dict[current.data] = 1
	# 		previous = current
	# 		current = current.next

	def removeDupes(self): 
		result_list = [self.head.data]
		current = self.head.next
		previous = self.head
		while current is not None: 
			if current.data in result_list: 
				previous.next = current.next
				current = current.next.next
			else: 
				result_list.append(current.data)
				previous = current
				current = current.next 






# test = LL()
# test.addNode(1)
# test.addNode(2)
# test.addNode(3)
# test.addNode(4)
# test.addNode(5)
# test.addNode(6)
# test.addNode(7)
# test.addNode(8)
# test.addNode(9)
# print str(test)
# print test.removeMiddle(5)
# # test.removeDupes()









