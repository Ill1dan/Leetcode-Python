class Solution(object):
    def countCollisions(self, directions):
        directions = directions.lstrip("L")
        directions = directions.rstrip("R")
        return len(directions) - directions.count("S")