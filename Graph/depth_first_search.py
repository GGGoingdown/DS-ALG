import queue
from typing import List, Dict


q : queue.LifoQueue = queue.LifoQueue()
marked_vertice: Dict = {}
finished_vertice: List = []

class Vertice:
    def __init__(self, value: int) -> None:
        self.value = value
        self.edges: List = []


def DFS(v: Vertice):
    marked_vertice[v.value] = 1
    print(f"Vertice: {v.value}")
    for v_edges in v.edges:
        if marked_vertice.get(v_edges.value) is None:
            DFS(v_edges) 

    finished_vertice.append(v.value)







def main():
    v0= Vertice(0)
    v1= Vertice(1)
    v2= Vertice(2)
    v3= Vertice(3)

    for v in [v1, v2, v3]:
        v0.edges.append(v)

    for v in [v0, v2, v3]:
        v1.edges.append(v)

    for v in [v0, v1]:
        v2.edges.append(v)

    for v in [v0, v1]:
        v3.edges.append(v)


    DFS(v3)

    print(finished_vertice)


main()
