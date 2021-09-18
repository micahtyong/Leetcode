"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# solution: bfs iter
# mem: o(n)
# time: o(n^2)

class BFSSolution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Idea: Maintain mapping from real to clone (bfs, queue)
        if node is None: return
        seen = { node: Node(node.val) }
        deque = collections.deque([node])
        while deque:
            currNode = deque.popleft() # pops from left side of queue 
            for neighbor in currNode.neighbors: 
                if neighbor not in seen:
                    seen[neighbor] = Node(neighbor.val)
                    deque.append(neighbor) # appends to right side of queue 
                seen[currNode].neighbors.append(seen[neighbor])
        return seen[node]

# solution: dfs iter
# mem: o(n) (stack and seen)
# time: o(n^2) for fully connected worst case 

class DFSIterSolution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Idea: Maintain mapping from real to clone
        if node is None: return
        seen = { node: Node(node.val) }
        stack = [node]
        while stack:
            currNode = stack.pop(0)
            for neighbor in currNode.neighbors: 
                if neighbor not in seen:
                    seen[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                seen[currNode].neighbors.append(seen[neighbor])
        return seen[node]

# solution: dfs recursive
# let n be the number of nodes.
# memory complexity: o(n)
# time complexity: o(n^2)
# exp: in a fully connected graph, there are n choose 2 edges = n(n−1)/2 => n^2

class DFSRecurSolution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Idea: Maintain mapping from real to clone
        if node is None: return
        seen = { node: Node(node.val) }
        self.dfs(node, seen)
        return seen[node]
     
    def dfs(self, node, seen):
        for neighbor in node.neighbors:
            if neighbor not in seen: 
                # visit! makes backward connection
                seen[neighbor] = Node(neighbor.val)
                self.dfs(neighbor, seen)
            # make forward connection
            seen[node].neighbors.append(seen[neighbor])
            