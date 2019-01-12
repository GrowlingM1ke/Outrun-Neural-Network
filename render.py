import pygame
import math
from util import Util as u

class Render:

    def __init__(self):
        self.colors = {}
        self.colors["grass"] = {"dark": (50, 248, 0), "light": (100, 248, 100)}
        self.Util = u()

    def loadScreen(self, screen, sky, hills, trees):
        screen.fill(0)
        screen.blit(sky, (0, 0))
        screen.blit(hills, (0, 100))
        screen.blit(trees, (0, 130))


    # TODO UNDERSTAND WTF IS GOING ON BELOW
    def loadRoad(self, variable, window):
        baseSegment = self.findSegment(variable)
        maxY = variable.height
        for x in range(0, variable.drawDistance):
            segment = variable.segments[(baseSegment.index + x) % len(variable.segments)]
            self.Util.project(segment.p1, variable)
            self.Util.project(segment.p2, variable)

            if segment.p1["camera"]["z"] <= variable.cameraDepth or segment.p2["screen"]["y"] >= maxY:
                continue

            self.drawSegment(window, segment, variable.width, variable.lanes)

            maxY = segment.p2["screen"]["y"]


    def findSegment(self, variable):
        return variable.segments[int(math.floor(variable.position/variable.segmentLength) % len(variable.segments))]

    def drawSegment(self, window, segment, width, lanes):
        x1 = segment.p1["screen"]["x"]
        y1 = segment.p1["screen"]["y"]
        x2 = segment.p2["screen"]["x"]
        y2 = segment.p2["screen"]["y"]
        pygame.draw.polygon(window, self.colors["grass"][segment.color], [(x1, y1), (x1 + width, y1),
                                                                             (x2 + width, y2), (x2, y2)])
