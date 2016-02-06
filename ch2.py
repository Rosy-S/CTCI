
from random import randint

class Node(object): 
	def __init__(self, value): 
		self.value = value
		self.next = None

class LinkedList(object): 
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self,value):
        node = Node(value)
        #if the old list is none, set new node as the first node
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def __str__(self):
        if self.head != None:
            index = self.head
            nodestore = [str(index.value)]
            while index.next != None:
                index = index.next
                nodestore.append(str(index.value))
            return "LinkedList  [ " + "->".join(nodestore) + " ]"
        return "LinkedList  []"

def randomLinkedList(length, min, max):
    linkedlist = LinkedList()
    for i in range(length):
        value = randint(min, max)
        linkedlist.addNode(value)
    return linkedlist

#1) write code to remove duplicates from an unsorted linked list

def remove_dupes(ll): 
	already_seen = set()
	current = ll.head
	while current.next != None: 
		if current.next.value in already_seen: 
			current.next = current.next.next

		else: 
			already_seen.add(current.value)
			current = current.next

def remove_dupes_nospace(ll): 
	pointer1 = ll.head
	while pointer1 != None:
		pointer2 = pointer1
		while pointer2.next != None: 
			if pointer1.value == pointer2.next.value: 
				pointer2.next = pointer2.next.next
			else: 
				pointer2 = pointer2.next
		pointer1 = pointer1.next

L1 = randomLinkedList(9, 3, 7)
# print L1
# print remove_dupes(L1)
# print L1

# L2 = randomLinkedList(9, 3, 7)
# print L2
# print remove_dupes_nospace(L2)
# print L2

#***************************************************************************************
#2) Return Kth to last element: 
def remove_kth_to_last_element(ll): 
	runner = ll.head
	start = runner
	while k > 0: 
		runner = runner.next
		k -= 1
	while runner.next != None: 
		runner = runner.next
		start = start.next
	return start.value 

#***************************************************************************************
#3) Delete the middle node only given access to the middle node: 
def delete_given_node(node): 
	replacement_value = node.next.value
	node.value = replacement_value
	node.next = node.next.next

#************************************************************************************
#4) Write code to partition a linked list around value x so that all nodes less than
# x are to the left and all nodes greater or equal are to the right

def partition(ll, x): 
	current = ll.head
	while current != None: 
		if current.value > x: 
			if current == ll.head: 
				ll.head = ll.head.next
			ll.tail.next = current
			current.next = None
		elif current.value < x and current != ll.head: 
			temp = ll.head.next
			ll.head.next = current
			current.next = temp
		else: 
			pass
		current = current.next
	
#*****************************************************************************************
# 5) write a function that adds the two nubers and returns the sum as a linked list for two 
# numbers represented as reversed in linked lists.
def reverse_add(ll1, ll2): 
	carryover = 0
	results = LinkedList()
	ll1_current = ll1.head
	ll2_current = ll2.head
	while carryover != 0 or ll1_current or ll2_current: 
		summ = 0
		if carryover: 
			summ += carryover
			carryover = 0
		if ll1_current: 
			summ += ll1_current.value
			ll1_current = ll1_current.next
		if ll2_current: 
			summ += ll2_current.value
			ll2_current = ll2_current.next
		if summ > 9: 
			carryover, summ = 1, summ - 10
		results.addNode(summ)
	return results

# L1 = randomLinkedList(3,0,9)
# L2 = randomLinkedList(5,0,9)
# print L1
# print L2
# print "In reverse order, the sum is: "
# print reverse_add(L1, L2)

#******************************************************************************************
#6) Implement a function to check if a linked list is a palindrome: 
def reverse_list_helper(ll): 
	first = ll.head
	second = ll.head.next
	temp = second
	first.next = None
	while second != None: 
		temp = second.next
		second.next = first
		first = second
		second = temp
	ll.head = first
	return ll 

import copy
def is_palindrome(ll1): 
	ll2 = copy.copy(ll1)	
	reverse_list_helper(ll2)
	return str(ll1) == str(ll2)


# L1 = LinkedList()
# L2 = LinkedList()
# [L1.addNode(x) for x in 'tacocatsss']
# [L2.addNode(x) for x in 'tacocat']
# print is_palindrome(L1)
# print is_palindrome(L2)

#****************************************************************************************
#7) Given two linked lists, determine if the two lists intersect and return the intersecting
# node that is the same node by reference in both lists. 

def find_ll_length(ll): 
	current = ll.head
	counter = 1
	while current.next != None: 
		current = current.next
		counter += 1
	return counter

def chop_off(ll, amount): 
	current = ll.head
	while amount > 0: 
		current = current.next
		amount -= 1
	ll.head = current

def find_ll_intersection(ll1, ll2): 
	ll1_length = find_ll_length(ll1)
	ll2_length = find_ll_length(ll2)

	if ll2_length > ll1_length: 
		amount_to_chop = ll2_length - ll1_length
		chop_off(ll2, amount_to_chop)

	elif ll1_length > ll2_length: 
		amount_to_chop = ll1_length - ll2_length
		chop_off(ll1, amount_to_chop)

	ll1_current = ll1.head
	ll2_current = ll2.head
	while ll1_current is not ll2_current and ll1_current:
		ll1_current = ll1_current.next
		ll2_current = ll2_current.next

	if ll1_current: 
		return ll1_current.value
	else: 
		return False

# L1 = LinkedList()
# L1.addNode(1)
# L1.addNode(2)
# L1.addNode(3)

# L2 = LinkedList()
# L2.addNode(3)
# node_4 = Node(4)
# node_5 = Node(5)
# node_6 = Node(6)

# L1.tail.next = node_4
# L1.tail = node_4
# L1.tail.next = node_5
# L1.tail = node_5
# L1.tail.next = node_6
# L1.tail = node_6
# L2.tail.next = node_4
# L2.tail = node_4
# L2.tail.next = node_5
# L2.tail = node_5
# L2.tail.next = node_6
# L2.tail = node_6

# print str(L1)
# print str(L2)
# print find_ll_intersection(L1, L2)

# L3 = randomLinkedList(5, 0, 9)
# L4 = randomLinkedList(3, 0, 9)
# print find_ll_intersection(L3, L4)


