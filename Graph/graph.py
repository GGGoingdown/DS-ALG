class GraphUsingDict:
    def __init__(self) -> None:
        self.number_of_nodes = 0
        self.adjacent_list: dict[int, set[int]] = {}

    def add_vertex(self, node_value: int) -> None:
        if self.adjacent_list.get(node_value) is None:
            self.adjacent_list[node_value] = set()

    def add_edge(self, node1_val: int, node2_val: int) -> None:
        if (node := self.adjacent_list.get(node1_val)) is None:
            raise Exception(f"Invalid node {node1_val!r}")

        node.add(node2_val)

    def show_connections(self) -> None:
        for v, edges in self.adjacent_list.items():
            print(f"Vertec - {v}, connections {[e for e in edges]}")


def main():
    graph = GraphUsingDict()
    for i in range(7):
        graph.add_vertex(i)
    
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 0)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 0)
    graph.add_edge(2, 1)
    graph.add_edge(2, 4)
    graph.add_edge(3, 1)
    graph.add_edge(3, 4)
    graph.add_edge(4, 3)
    graph.add_edge(4, 2)
    graph.add_edge(4, 5)
    graph.add_edge(5, 4)
    graph.add_edge(5, 6)
    graph.add_edge(6, 5)

    graph.show_connections()

main()