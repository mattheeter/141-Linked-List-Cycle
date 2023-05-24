# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

def hasCycle(self, head: Optional[ListNode]) -> bool:
    # Thinking best solution is to look through each node and see if its next attribute is less than the one before it