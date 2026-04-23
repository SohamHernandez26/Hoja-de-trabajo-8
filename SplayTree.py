from Nodo import Nodo 

class SplayTree:

    def __init__(self):
        self.root = None
    
    def rotate_left(self, x):
        y = x.right
        if y is None:
            return
        
        x.right = y.left
        if y.left:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y

    def rotate_right(self, x):
        y = x.left
        if y is None:
            return
        
        x.left = y.right
        if y.right:
            y.right.parent = x
        
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.left = y
    
    def splay(self, x):
        while x.parent:
            if x.parent.parent is None:
                # Zig
                if x.parent.left == x:
                    self.rotate_right(x.parent)
                else:
                    self.rotate_left(x.parent)
            else:
                # Zig-Zig o Zig-Zag
                if x.parent.left == x and x.parent.parent.left == x.parent:
                    self.rotate_right(x.parent.parent)
                    self.rotate_right(x.parent)
                elif x.parent.right == x and x.parent.parent.right == x.parent:
                    self.rotate_left(x.parent.parent)
                    self.rotate_left(x.parent)
                elif x.parent.left == x:
                    self.rotate_right(x.parent)
                    self.rotate_left(x.parent)
                else:
                    self.rotate_left(x.parent)
                    self.rotate_right(x.parent)

    def insert(self, proceso):
        nuevo = Nodo(proceso)

        if self.root is None:
            self.root = nuevo
            return

        current = self.root
        while True:
            if proceso.vruntime < current.proceso.vruntime:
                if current.left is None:
                    current.left = nuevo
                    nuevo.parent = current
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = nuevo
                    nuevo.parent = current
                    break
                current = current.right

        self.splay(nuevo)

    def search(self, vruntime):
        current = self.root
        steps = 0

        while current:
            steps += 1

            if vruntime == current.proceso.vruntime:
                self.splay(current)
                return current, steps
            elif vruntime < current.proceso.vruntime:
                current = current.left
            else:
                current = current.right

        return None, steps


    
    