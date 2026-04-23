import random
from Proceso import Proceso
from BST import BST
from SplayTree import SplayTree
from RedBalckTree import RedBlackTree




def escenario_A():
    procesos = [Proceso(i, random.randint(1, 10000)) for i in range(1000)]

    bst = BST()
    splay = SplayTree()
    rb = RedBlackTree()

    for p in procesos:
        bst.insert(p)
        splay.insert(p)
        rb.insert(p)

    muestras = random.sample(procesos, 100)

    total_bst = total_splay = total_rb = 0

    for p in muestras:
        _, a = bst.search(p.vruntime)
        _, b = splay.search(p.vruntime)
        _, c = rb.search(p.vruntime)

        total_bst += a
        total_splay += b
        total_rb += c

    print("\nEscenario A:")
    print("BST:", total_bst / 100)
    print("Splay:", total_splay / 100)
    print("Red-Black:", total_rb / 100)
    pass

def escenario_B():
     # 1. Crear procesos ordenados
    procesos = []
    for i in range(1, 1001):
        procesos.append(Proceso(i, i))

    # 2. Crear árboles
    bst = BST()
    splay = SplayTree()
    rb = RedBlackTree()

    # 3. Insertar
    for p in procesos:
        bst.insert(p)
        splay.insert(p)
        rb.insert(p)

    # 4. Buscar el último
    _, steps_bst = bst.search(1000)
    _, steps_splay = splay.search(1000)
    _, steps_rb = rb.search(1000)

    # 5. Mostrar resultados
    print("Escenario B:")
    print("BST:", steps_bst)
    print("Splay:", steps_splay)
    print("Red-Black:", steps_rb)
    pass

def escenario_C():
    # después lo haremos
    pass


if __name__ == "_main_":
    escenario_A()
    escenario_B()