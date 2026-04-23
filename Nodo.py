class Nodo:
    def __init__(self, proceso):
        self.proceso = proceso
        self.left = None
        self.right = None
        self.parent = None
        
        self.color = "red"