from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._fermate = DAO.getAllFermate()
        self._grafo = nx.DiGraph()
        self._idMap = {}
        for f in self._fermate:
            self._idMap[f._id_fermata] = f

    def buildGraph(self):
        self._grafo.add_nodes_from(self._fermate)
        # Metodo 1: troppo lento
        # for u in self._fermate:
        #     for v in self._fermate:
        #         res = DAO.getEdge(u, v)
        #         if len(res) > 0:
        #             self._grafo.add_edge(u, v)
        #             print(f"Aggiunto {u} e {v}")

        # Metodo 2: ho bisogno di costruire uma dizionario (idMap) per recuperare id_fermata da id_stazP
        # for u in self._fermate:
        #     vicini = DAO.getEdgeVicini(u)
        #     for v in vicini:
        #         v_nodo = self._idMap[v._id_stazA]
        #         self._grafo.add_edge(u, v_nodo)
        #         print(f"Aggiunto {u} e {v}")

        # Metodo 3: leggo tutti i dati
        all_connessioni = DAO.getAllConnessioni()
        for c in all_connessioni:
            u_nodo = self._idMap[c._id_stazP]
            v_nodo = self._idMap[c._id_stazA]
            self._grafo.add_edge(u_nodo, v_nodo)
            print(f"Aggiunto {u_nodo} e {v_nodo}")

    @property
    def fermate(self):
        return self._fermate

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)



