class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        finishing_order = []
        for i in range(0, len(order), 1):
            if order[i] in friends:
                finishing_order.append(order[i])
        return finishing_order


        