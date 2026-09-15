class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        border_points = set()
        
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            # Symmetric difference cleanly toggles points in the set
            border_points ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
            
        if len(border_points) != 4:
            return False
        
        # Extract the global bounding box from the 4 remaining corners
        x1, y1, x2, y2 = (
            min(x for x, _ in border_points),
            min(y for _, y in border_points),
            max(x for x, _ in border_points),
            max(y for _, y in border_points)
        )
        
        return area == (x2 - x1) * (y2 - y1)