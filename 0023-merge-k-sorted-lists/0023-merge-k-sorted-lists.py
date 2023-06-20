# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, nums: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        if not nums: return None
        for i in range(len(nums)):
            while nums[i]:
                res.append(nums[i].val)
                nums[i] = nums[i].next
        if not res:return None
        res.sort()
        head = ListNode(res[0])
        curr = head
        for i in range(1, len(res)):
            newnode = ListNode(res[i])
            curr.next = newnode
            curr = newnode
        return head