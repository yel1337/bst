class Tree:
    def __init__(self, points):
        self.left_plane = None
        self.right_plane = None
        self.points = points
        self.n_points = len(points)
    
    def root_of_tree(self):
        # Separate root from points
        # Usually we take first index as the root of the tree
        return self.points[0]

    def insert(self, root):
        # Start with the first index of the array as the root
        r = self.root_of_tree()
        
        for i in range(1, self.n_points):
            if self.points[i] > r:
                self.left_plane = self.insert(self.points[i])
                self.n = self.points[i]
            else:
                self.right_plane = self.insert(self.points[i])
                self.n = self.points[i]
                
    def traverse(self, node=None, depth=0): # Normal Tree Traversal
        if node is None:
            node = self.n
            
        if self.left_plane:
            self.traverse(node, depth+1)
        if self.right_plane:
            self.traverse(node, depth+1)
  
