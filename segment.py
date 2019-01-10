

class Segment:

    def __init__(self, index, variable, color):
        self.index = index
        self.p1 = {"world": {"x": {}, "y": {}, "z": (index * variable.segmentLength)}, "camera": {}, "screen": {}}
        self.p2 = {"world": {"x": {}, "y": {}, "z": ((index + 1) * variable.segmentLength)}, "camera": {}, "screen": {}}
        self.color = color
