class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        tail = head

        for _ in range(k):
            if not tail:
                return head
            tail = tail.next

        def reverse(cur, end):
            prev = None

            while cur != end:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next

            return prev      

        new_head = reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)

        return new_head            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna