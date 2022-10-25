import queue
from typing import List

class Vertice:
    def __init__(self, value: int) -> None:
        self.value = value
        self.edges: List = []


def BST(v: Vertice) -> List:
    mark_vertices = {}
    q: queue.Queue = queue.Queue()

    for v_edges in v.edges:
        q.put(v_edges)
        mark_vertices[v_edges.value] = 1

    while not q.empty():
        get_v = q.get()
        for v_edges in get_v.edges:
            if mark_vertices.get(v_edges.value) is None:
                mark_vertices[v_edges.value] = 1
                q.put(v_edges)

    return [*mark_vertices]

def main():
    v0= Vertice(0)
    v1= Vertice(1)
    v2= Vertice(2)
    v3= Vertice(3)
    v4= Vertice(4)
    v5= Vertice(5)
    v6= Vertice(6)
    v7= Vertice(7)

    for v in [v1, v7, v3, v6]:
        v0.edges.append(v)

    for v in [v0, v7, v3, v4, v2]:
        v1.edges.append(v)

    for v in [v1, v5]:
        v2.edges.append(v)

    for v in [v0, v1, v5]:
        v3.edges.append(v)

    for v in [v1, v7]:
        v4.edges.append(v)

    for v in [v3, v2]:
        v5.edges.append(v)

    for v in [v0]:
        v6.edges.append(v)

    for v in [v0, v1, v4]:
        v7.edges.append(v)



    print(BST(v7))


main()