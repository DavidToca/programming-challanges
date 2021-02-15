class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:       
        sets = {}
        n_nodes = len(graph)
        queue = []
        
        for node, edges in enumerate(graph):
            if edges == []:
                continue

            queue.append(node)

            if node not in sets:
                sets[node] = 'A'

            while(len(queue)):
                current_node = queue.pop(0)

                node_set = sets[current_node] # A/B

                for edge in graph[current_node]:

                    if edge not in sets:
                        sets[edge] = 'A' if node_set == 'B' else 'B'
                        queue.append(edge)

                    if sets[edge] == node_set:
                        return False

        return True