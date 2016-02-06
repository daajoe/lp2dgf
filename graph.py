class Graph(object):
    def __init__(self):
        self.__edges=set()
        self.__tab=dict()

    def add_edge(self,x,y):
        self.__edges.add((self.__vertex_id(x),self.__vertex_id(y)))

    def __vertex_id(self,x):
        if self.__tab.has_key(x):
            return self.__tab[x]
        else:
            self.__tab[x]=len(self.__tab)+1
            return self.__tab[x]

    def edge_iter(self):
        return iter(self.__edges)

    
    def __iter__(self):
        return self.edge_iter()

    def num_edges(self):
        return len(self.__edges)

    def num_vertices(self):
        return len(self.__tab)
