import itertools as it
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def createGrafo():
    myGraph = nx.Graph()
    f = open(r"idro1.txt","r")
    radice = f.readline().strip()
    print(f"Radice: {radice}")
    riga = f.readline()
    while riga != "":
        riga = riga.strip()
        id, start_nodo, end_nodo, lung = riga.split("\t")
        #print(f"id {id} start_nodo {start_nodo} end_nodo {end_nodo} lunghezza {lung}")
        myGraph.add_edge(start_nodo, end_nodo,id=id, dist=lung)
        riga = f.readline()
    f.close()

    print(myGraph['73'])

    nx.draw(myGraph, with_labels=False)
    plt.show()

    #plt.savefig("filename.png")

if __name__ == '__main__':
    createGrafo()
