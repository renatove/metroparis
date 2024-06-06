from model.model import Model

def start():
    model = Model()
    model.buildGraph()
    print(f"Numero nodi: {model.getNumNodes()}")
    print(f"Numero edges: {model.geuNumEdges()}")

# testing
if __name__ == '__main__':
    start()
