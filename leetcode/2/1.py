# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l3 = []
        print("l1:", l1)
        print("l2:", l2)
        # Make sure both lists are the same length
        for i in range(min(len(l1), len(l2))):
            l3.append(l1[i] + l2[i])
        return l3[::-1]

# Example call:
s = Solution()
result = s.addTwoNumbers([2, 3, 4, 5], [5, 6, 4])
print("Result:", result)