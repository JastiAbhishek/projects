import ArrayQueue

ans = []
class BinaryTree:
    class Node:
        def __init__(self, x : object, v = None) :
            self.parent = self.left = self.right = None
            self.x = x
            self.v = v

        def set_key(self, x) :
            self.x = x

        def set_val(self, v):
            self.v = v

        def insert_left(self) :
            self.left = BinaryTree.Node('') 
            self.left.parent = self
            return self.left

        def insert_right(self) :
            self.right = BinaryTree.Node('')
            self.right.parent = self
            return self.right

        def __str__(self):
            if self.v is None:
                return str(self.x)
            return f"({self.x}, {self.v})"

    def __init__(self) : 
        self.r = None

    def depth(self, u : Node) -> int:
        temp = u
        d = 0
        while temp != self.r:
            temp = temp.parent
            d += 1
        return d

    def _size(self, u : Node) -> int:
        if u == None:
            return 0
        return 1+self._size(u.left) + self._size(u.right)

    def size(self) -> int:
        return self._size(self.r)

    def size2(self) -> int:
        u = self.r
        previous = None
        n = 0
        while u != None:
            if previous == u.parent:
                n = n + 1
                if u.left != None:
                    nxt = u.left
                elif u.right != None:
                    nxt = u.right
                else:
                    nxt = u.parent
            elif previous == u.left:
                if u.right != None:
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            previous = u
            u = nxt
        return n

    def _height(self, u: Node) -> int:
        if u == None:
            return 0
        return 1 + max(self._height(u.left), self._height(u.right))

    def height(self) -> int:
        return self._height(self.r)
    
    def _in_order(self, u : Node) -> list:
        if u == None:
            return
        else:
            self._in_order(u.left)
            ans.append(u)
            self._in_order(u.right)
        return ans

    def in_order(self) -> list:
        ans.clear()
        return self._in_order(self.r)

    def _pre_order(self, u : Node) -> list:
        if u == None:
            return
        else:
            ans.append(str(u))
            self._pre_order(u.left)
            self._pre_order(u.right)
        return ans
        
        # if u == None:
        #     return ans
        # if u.right == None and u.left == None:
        #     ans.append(str(u))
        #     return
        # return(str(u), self._pre_order(u.left), self._pre_order(u.right))

    def pre_order(self) -> list:
        ans.clear()
        return self._pre_order(self.r)

    def _post_order(self, u : Node) -> list:
        if u == None:
            return
        else:
            self._post_order(u.left)
            self._post_order(u.right)
            ans.append(str(u))
        return ans

    def post_order(self) -> list:
        ans.clear()
        return self._post_order(self.r)

    def bf_traverse(self):
        arr = []
        queue = ArrayQueue.ArrayQueue()
        if self.r != None:
            queue.add(self.r)
        while(queue.size() != 0):
            u = queue.remove()
            arr.append(u)
            if(u.left != None):
                queue.add(u.left)
            if(u.right != None):
                queue.add(u.right)
        return arr

    def first_node(self):
        w = self.r
        if w is None: return None
        while w.left != None:
            w = w.left
        return w
    
    def next_node(self, w):
        if w.right is not None:
            w = w.right
            while w.left is not None:
                w = w.left
        else:
            while w.parent is not None and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

    def __str__(self):
        nodes = self.bf_traverse()
        nodes_str = [str(node) for node in nodes]
        return ', '.join(nodes_str)