class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# The objects that we want stored in the quadtree
class Node:
    def __init__(self, pos, data):
        self.pos = pos
        self.data = data
 
# The main quadtree class
class Quad:
    def __init__(self, topL, botR):
        self.topLeft = topL
        self.botRight = botR
        self.n = None #Node stored directly in the current quad if it's a leaf node.
        
        #child of a quard tree
        self.topLeftTree = None
        self.topRightTree = None
        self.botLeftTree = None
        self.botRightTree = None
 
    # Insert a node into the quadtree
    def insert(self, node):
        if node is None:
            return
 
        # Current quad cannot contain it
        if not self.inBoundary(node.pos):
            return
 
        # We are at a quad of unit area
        # We cannot subdivide this quad further
        if abs(self.topLeft.x - self.botRight.x) <= 1 and abs(self.topLeft.y - self.botRight.y) <= 1:
            if self.n is None:
                self.n = node
            return
 
        if (self.topLeft.x + self.botRight.x) / 2 >= node.pos.x:
            # Indicates topLeftTree
            if (self.topLeft.y + self.botRight.y) / 2 >= node.pos.y:
                if self.topLeftTree is None:
                    self.topLeftTree = Quad(self.topLeft, Point((self.topLeft.x + self.botRight.x) / 2, (self.topLeft.y + self.botRight.y) / 2))
                self.topLeftTree.insert(node)
            # Indicates botLeftTree
            else:
                if self.botLeftTree is None:
                    self.botLeftTree = Quad(Point(self.topLeft.x, (self.topLeft.y + self.botRight.y) / 2), Point((self.topLeft.x + self.botRight.x) / 2, self.botRight.y))
                self.botLeftTree.insert(node)
        else:
            # Indicates topRightTree
            if (self.topLeft.y + self.botRight.y) / 2 >= node.pos.y:
                if self.topRightTree is None:
                    self.topRightTree = Quad(Point((self.topLeft.x + self.botRight.x) / 2, self.topLeft.y), Point(self.botRight.x, (self.topLeft.y + self.botRight.y) / 2))
                self.topRightTree.insert(node)
            # Indicates botRightTree
            else:
                if self.botRightTree is None:
                    self.botRightTree = Quad(Point((self.topLeft.x + self.botRight.x) / 2, (self.topLeft.y + self.botRight.y) / 2), self.botRight)
                self.botRightTree.insert(node)
 
    # Find a node in a quadtree
    def search(self, p):
        # Current quad cannot contain it
        if not self.inBoundary(p):
            return 0  # Return 0 if point is not found
 
        # We are at a quad of unit length
        # We cannot subdivide this quad further
        if self.n is not None:
            return self.n
 
        if (self.topLeft.x + self.botRight.x) / 2 >= p.x:
            # Indicates topLeftTree
            if (self.topLeft.y + self.botRight.y) / 2 >= p.y:
                if self.topLeftTree is None:
                    return 0
                return self.topLeftTree.search(p)
            # Indicates botLeftTree
            else:
                if self.botLeftTree is None:
                    return 0
                return self.botLeftTree.search(p)
        else:
            # Indicates topRightTree
            if (self.topLeft.y + self.botRight.y) / 2 >= p.y:
                if self.topRightTree is None:
                    return 0
                return self.topRightTree.search(p)
            # Indicates botRightTree
            else:
                if self.botRightTree is None:
                    return 0
                return self.botRightTree.search(p)
 
    # Check if current quadtree contains the point
    def inBoundary(self, p):
        return p.x >= self.topLeft.x and p.x <= self.botRight.x and p.y >= self.topLeft.y and p.y <= self.botRight.y
 
# Driver program
center = Quad(Point(0, 0), Point(8, 8))
a = Node(Point(1, 1), 1)
b = Node(Point(2, 5), 4)
c = Node(Point(7, 6), 3)
d = Node(Point(5, 5), 0)
center.insert(a)
center.insert(b)
center.insert(c)
print("Node a:", center.search(Point(1, 1)).data)
print("Node b:", center.search(Point(2, 5)).data)
print("Node c:", center.search(Point(7, 6)).data)
print("Non-existing node:", center.search(Point(5, 5)))