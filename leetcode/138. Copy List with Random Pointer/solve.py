"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:

    equivalence = {}

    def copy_node(self, node, index):
        if not node:
            return None
        node.index = index
        copy_node = Node(node.val, None, node.random)
        
        self.equivalence[index] = copy_node
        
        return copy_node
        
    
    def copy(self, root):
        if not root:
            return root
        index = 0
        copy_root = self.copy_node(root, index)
        
        copy_before_node = copy_root
        
        before_node = root
        
        while(before_node.next):
            index+=1
            copy_node = self.copy_node(before_node.next, index)
            copy_before_node.next = copy_node
            
            before_node = before_node.next
            copy_before_node = copy_node
        
        return copy_root
        
    def link_random(self, copy_head):
        current = copy_head
        while(current):
            if current.random:
                current.random = self.equivalence[current.random.index]
            current = current.next
        return copy_head

    def copyRandomList(self, head: 'Node') -> 'Node':
        self.equivalence = {}

        copy_head = self.copy(head)
        copy_head = self.link_random(copy_head)
        
        return copy_head
