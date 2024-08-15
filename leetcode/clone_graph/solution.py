from typing import Optional


# Definition for a Node.
#
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return

        stack: list[Node] = [node]
        created = {}

        while stack:
            curr = stack.pop()
            # if the curr node is not cloned yet, we clone it without any neighbors
            if curr.val not in created:
                created[curr.val] = Node(val=curr.val)

            cloned_node = created[curr.val]

            if curr.neighbors:
                # loop through all the neighbors and clone it if not cloned, if not cloned we append to the stack for later access
                # because later, we pop the real neighbor -> get the clone and then loop neighbors of the neighbor -> get all cloned neighbor and update the cloned neighbor's neighbors
                # we append all the neighbors for the clone node.
                for neighbor in curr.neighbors:
                    if neighbor.val not in created:
                        created[neighbor.val] = Node(val=neighbor.val)
                        stack.append(neighbor)
                    cloned_node.neighbors.append(created[neighbor.val])

        return created[node.val]
