class AVLTree:
    # Constructor:
    def __init__(self,initval=None):
        self.value = initval
        if self.value:
            self.left = AVLTree()
            self.right = AVLTree()
            self.height = 1
        else:
            self.left = None
            self.right = None
            self.height = 0
        return

    def isempty(self):
        return (self.value == None)

    def isleaf(self):
        return (self.value != None and self.left.isempty() and self.right.isempty())

    def leftrotate(self):
        v = self.value
        vr = self.right.value
        tl = self.left
        trl = self.right.left
        trr = self.right.right
        newleft = AVLTree(v)
        newleft.left = tl
        newleft.right = trl
        self.value = vr
        self.right = trr
        self.left = newleft
        return
    def rightrotate(self):
        v = self.value
        vl = self.left.value
        tll = self.left.left
        tlr = self.left.right
        tr = self.right
        newright = AVLTree(v)
        newright.left = tlr
        newright.right = tr
        self.right = newright
        self.value = vl
        self.left = tll
        return
    def insert(self,v):
        if self.isempty():
            self.value = v
            self.height = 1
            self.right = AVLTree()
            self.left = AVLTree()
            self.rebalance(v)
        
        elif self.value == v:
            return
        
        elif v < self.value:
            self.left.insert(v)
            self.rebalance(v)
            return
            
        
        elif v > self.value:
            self.right.insert(v)
            self.rebalance(v)
            return
    
    def calc_height(self):
        if self.valve == None:
            return
        
        else:
            return (1 + max(self.left.hight, self.right.height))
            
    def rebalance(self,v):
        slope = self.left.height - self.right.height
        if slope > 1 and v < self.left.value:
            self.rightrotate()
            self.height = 1 + max(self.left.height,self.right.height)
            self.left.height = 1 + max(self.left.left.height,self.right.right.height)
            self.right.height = 1 + max(self.left.left.height,self.right.right.height)
        
        if slope < -1 and v > self.right.value:
            self.leftrotate()
            self.height = 1 + max(self.left.height,self.right.height)
        
        if slope > 1 and v > self.left.value:
           
            self.left.leftrotate()
            self.rightrotate()
            self.left.height = 1 + max(self.left.left.height,self.right.right.height)
            self.right.height = 1 + max(self.left.left.height,self.right.right.height)
        
        if slope < -1 and v < self.right.value:
            self.right.rightrotate()
            self.leftrotate()
            self.left.height = 1 + max(self.left.left.height,self.right.right.height)
            self.right.height = 1 + max(self.left.left.height,self.right.right.height)
        
        self.height = 1 + max(self.left.height,self.right.height)
        return
       
    def inorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.inorder()+ [self.value]+ self.right.inorder())
    def preorder(self):
        if self.isempty():
            return([])
        else:
            return([self.value] + self.left.preorder()+  self.right.preorder())
    def postorder(self):
        if self.isempty():
            return([])
        else:
            return(self.left.postorder()+ self.right.postorder() + [self.value])

A = AVLTree()
nodes = eval(input())
for i in nodes:
    A.insert(i)

print(A.inorder())
print(A.preorder())
print(A.postorder())