"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashmap = {}

        curr, prev = head, Node(0)
        prev_clone = Node(0)
        # create clone and add key value pairs to hashmap in one go
        while prev:
            if curr == None:
                curr_clone = None
            else: 
                curr_clone = Node(curr.val, None, None)

            prev_clone.next = curr_clone
            hashmap[prev] = prev_clone

            prev_clone = curr_clone
            prev = curr
            if curr == None:
                curr = None
            else:
                curr = curr.next

        curr = head
        curr_clone = hashmap.get(head)

        while curr:
            curr_clone.random = hashmap.get(curr.random)
            curr = curr.next
            curr_clone = curr_clone.next

        return hashmap.get(head)
# we keep a hashmap where key is original.object and value is cloned.object
# we iterate through the original linked list
# for each key node's random value, we append its hashmap value's random reference with the value at the key the original node's random is pointing to