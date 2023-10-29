import graphviz
class DirectedGraph:
    def __init__(self, num_vertices, weighted):
        self.adj_list = [None] * num_vertices
        self.with_weights = weighted
        for i in range(num_vertices):
            self.adj_list[i] = []

    def add_to_adj_list(self, edges):
        for edge in edges:
            if self.with_weights: #This is a weighted directed graph
                src, dest, weight = edge
                self.adj_list[src].append((dest, weight))
            else: #Just a directed graph
                src, dest = edge
                self.adj_list[src].append(dest)
    
    def visualize_graph(self):
        dot = graphviz.Digraph()

        def add_node_edges(src, edges):
            for edge in edges:
                if self.with_weights:
                    dot.node(str(src))
                    dot.edge(str(src), str(edge[0]), weight=str(edge[1]), label=str(edge[1]))
                else:
                    dot.node(str(src))
                    dot.edge(str(src), str(edge))
        
        for src, edges in enumerate(self.adj_list):
            add_node_edges(src, edges)
        
        return dot
    
    def dfs(self, vertex, visited):
        visited.add(vertex)

        print(vertex, end=" --> ")
        
        for adj_edge in self.adj_list[vertex]:
            if adj_edge not in visited:
                self.dfs(adj_edge, visited)

    def bfs(self, vertex):
        visited = [False] * (len(self.adj_list) + 1)

        queue = list()
        queue.append(vertex)
        visited[vertex] = True

        while queue:
            curr_vertex = queue.pop(0)
            print(curr_vertex, end=" --> ")
            for edge in self.adj_list[curr_vertex]:
                if visited[edge] == False:
                    visited[edge] = True
                    queue.append(edge)


    def print_adj_paths(self):
        for src, path in enumerate(self.adj_list):
            for adj_path in path:
                if self.with_weights:
                    dest, weight = adj_path
                    print(f"Edge Node: {src} --> {dest} (Dest edge Node). With {weight} weight")
                else:
                    print(f"Edge Node: {src} --> {adj_path} (Dest edge Node).")

def main():
    num_vertices = 6
    edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2),
            (4, 5), (5, 4)]
    graph_weighted = False
    direct_graph_obj = DirectedGraph(num_vertices, graph_weighted)
    direct_graph_obj.add_to_adj_list(edges)
    direct_graph_obj.print_adj_paths()

    num_vertices = 6
    edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10),
            (4, 5, 1), (5, 4, 3)]
    graph_weighted = True
    weighted_direct_graph_obj = DirectedGraph(num_vertices, graph_weighted)
    weighted_direct_graph_obj.add_to_adj_list(edges)
    weighted_direct_graph_obj.print_adj_paths()

if __name__ == "__main__":
    main()
