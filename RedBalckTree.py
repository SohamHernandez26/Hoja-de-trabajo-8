from Nodo import Nodo
from Proceso import Proceso

class RedBlackTree:
    def __init__(self):
        self.NodoFantasma = Nodo(Proceso(-1, -1))
        self.NodoFantasma.color = 0  # negro
        self.NodoFantasma.left = self.NodoFantasma
        self.NodoFantasma.right = self.NodoFantasma
        self.root = self.NodoFantasma

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NodoFantasma:
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

    def right_rotate(self, y):
        x = y.left
        y.left = x.right

        if x.right != self.NodoFantasma:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def arreglar(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)

                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)

                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)

            if k == self.root:
                break

        self.root.color = 0

    def insert(self, proceso):
        nuevo_nodo = Nodo(proceso)
        nuevo_nodo.left = self.NodoFantasma
        nuevo_nodo.right = self.NodoFantasma
        nuevo_nodo.color = 1

        padre = None
        actual = self.root

        while actual != self.NodoFantasma:
            padre = actual
            if proceso.vruntime < actual.proceso.vruntime:
                actual = actual.left
            else:
                actual = actual.right

        nuevo_nodo.parent = padre

        if padre is None:
            self.root = nuevo_nodo
        elif proceso.vruntime < padre.proceso.vruntime:
            padre.left = nuevo_nodo
        else:
            padre.right = nuevo_nodo

        if nuevo_nodo.parent is None:
            nuevo_nodo.color = 0
            return

        if nuevo_nodo.parent.parent is None:
            return

        self.arreglar(nuevo_nodo)

    def search(self, vruntime):
        actual = self.root
        pasos = 0

        while actual != self.NodoFantasma:
            pasos += 1

            if vruntime == actual.proceso.vruntime:
                return actual, pasos

            elif vruntime < actual.proceso.vruntime:
                actual = actual.left
            else:
                actual = actual.right

        return None, pasos