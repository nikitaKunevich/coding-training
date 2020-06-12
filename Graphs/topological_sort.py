from collections import deque

class SolutionOne:
    '''
    1. Find nodes that doesn't have prerequisites,
    2. add them to result array and remove all dependencies on those nodes from the
    graph.
    3. Check if nodes with removed dependencies now don't have prerequisites and if 
    they don't - repeat the step 2.
    '''

    # O(j+d) time | O(j + d) space
    def topologicalSort(self, jobs, deps):
        node_prerequisites, prerequisite_nodes, no_prereq_nodes = self.buildAuxiliaryDicts(jobs, deps)
        result = []
        while no_prereq_nodes: # check for emptiness
            node = no_prereq_nodes.pop()
            result.append(node)
            for child_node in prerequisite_nodes[node]:
                child_prereqs = node_prerequisites[child_node]
                child_prereqs.remove(node)
                if len(child_prereqs) == 0:
                    no_prereq_nodes.appendleft(child_node)
        if len(result) < len(jobs):
            return []
        return result

    # O(j + d) time | O(j + d) space
    def buildAuxiliaryDicts(self, jobs, deps):
        node_prerequisites, prerequisite_nodes = {x:set() for x in jobs}, {x:[] for x in jobs}
        no_prereq_nodes = deque()
        for dep in deps:
            prereq, node = dep
            node_prerequisites[node].add(prereq)
            prerequisite_nodes[prereq].append(node)
        for job in jobs:
            if len(node_prerequisites[job]) == 0:
                no_prereq_nodes.appendleft(job)
            
        return node_prerequisites, prerequisite_nodes, no_prereq_nodes
