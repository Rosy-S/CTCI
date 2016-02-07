class BinaryTree:
    def __init__(self, content):
        self.content = content
        self.left = None
        self.right = None
        #-1 means the depth has not been calculated yet.
        self.depth = -1

    def __str__(self):
        return "( " + str(self.content) + " ( " + str(self.left) + " | " + str(self.right) + "))" 


#****************************************************************************************
#2) Given a sorted array with unique integer elements, write an algorithm to create
# a binary search tree with minimal height