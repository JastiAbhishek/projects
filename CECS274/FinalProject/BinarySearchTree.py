from BinaryTree import BinaryTree
from Interfaces import Set


class BinarySearchTree(BinaryTree, Set):

    def __init__(self):
        BinaryTree.__init__(self)
        self.n = 0
        
    def clear(self):
        self.r = None
        self.n = 0

    def new_node(self, x):
        u = BinaryTree.Node(x)
        u.left = u.right = u.parent = None
        return u

    def find_eq(self, x : object) -> object:
        temp = self.r
        while temp != None:
            if x < temp.x:
                temp = temp.left
            elif x > temp.x:
                temp = temp.right
            else:
                return temp
        return None
        
    def find_last(self, x : object) -> BinaryTree.Node:
        w = self.r
        previous = None
        while w != None:
            previous = w
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return previous

    def find(self, x: object) -> object:
        w = self.r
        z = None
        while w != None:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w
        return z
        
    def add_child(self, p : BinaryTree.Node, u : BinaryTree.Node) -> bool:
        if p == None:
            self.r = u
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False
            u.parent = p
        self.n = self.n + 1
        return True
        
    def add_node(self, u : BinaryTree.Node) -> bool:
        p = self.find_last(u.x)
        return self.add_child(p, u)

    def add(self, key : object, value : object) -> bool:
        if self.r == None:
            self.r = self.new_node(key)
            self.r.set_val(value)
            self.n = self.n + 1
            return True
        else:
            w = self.new_node(key)
            w.set_val(value)
            p = self.find_last(key)
            a = self.add_child(p, w)
            return a

    def get(self, key : object) -> object:
        w = self.find_eq(key)
        if(w != None):
            return w.v
        return None
    
    def splice(self, u: BinaryTree.Node):
        if u.left != None:
            s = u.left
        else:
            s = u.right
        p = None
        if self.r == u:
            self.r = s
        else:
            p = u.parent
            if u == p.left:
                p.left = s
            else:
                p.right = s
        if s != None:
            s.parent = p
        self.n = self.n - 1

    def remove_node(self, u : BinaryTree.Node):
        if u != None:
            temp = u.v
            if u.right == None or u.left == None:
                self.splice(u)
            else:
                w = u.right
                while w.left != None:
                    w = w.left
                u.x = w.x
                u.v = w.v
                self.splice(w)
            return temp
        return None

    def remove(self, x : object) -> bool:
        w = self.find_eq(x)
        if(w != None): 
            return self.remove_node(w)
        else:
            raise ValueError
        
             
    def __iter__(self):
        u = self.first_node()
        while u is not None:
            yield u.x
            u = self.next_node(u)


            
