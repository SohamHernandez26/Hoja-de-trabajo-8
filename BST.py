from nodo import Nodo

class BST:
    def __init__(self):
        self.root = None

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
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = nuevo
                    nuevo.parent = current
                    return
                current = current.right

    def search(self, vruntime):
        current = self.root
        steps = 0

        while current:
            steps += 1

            if vruntime == current.proceso.vruntime:
                return current, steps
            elif vruntime < current.proceso.vruntime:
                current = current.left
            else:
                current = current.right

        return None, steps