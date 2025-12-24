class Solution(object):
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)
        
        capacity.sort(reverse=True)
        
        boxes = 0
        for c in capacity:
            total_apples -= c
            boxes += 1
            if total_apples <= 0:
                break
        
        return boxes
        