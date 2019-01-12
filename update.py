import pygame
from util import Util as u
import math
from segment import Segment

class Update:

    def __init__(self):
        self.Util = u()

    # A fixed time step ensures that are physics are independent of fps change
    def fixTimeStep(self, variable, keys):
        variable.currentFrame = pygame.time.get_ticks()
        variable.deltaTime = (variable.currentFrame - variable.LastFrame) / 1000.0
        variable.gDeltaTime += variable.deltaTime
        while variable.gDeltaTime > variable.step:
            variable.gDeltaTime -= variable.step
            if len(variable.segments) == 0:
                self.resetRoad(variable)
            self.update(variable, keys)
        variable.LastFrame = variable.currentFrame

    # update the world based on what the player has input
    def update(self, variable, keys):
        variable.position = self.Util.increase(variable.position, variable.step * variable.speed, variable.trackLength)
        dx = variable.step * 2 * (variable.speed/variable.maxSpeed)

        if keys[1]:
            variable.playerX -= dx
        elif keys[3]:
            variable.playerX += dx

        if keys[0]:
            variable.speed = self.Util.accelerate(variable.speed, variable.accelerate, variable.step)
        elif keys[2]:
            variable.speed = self.Util.accelerate(variable.speed, variable.breaking, variable.step)
        else:
            variable.speed = self.Util.accelerate(variable.speed, variable.decelerate, variable.step)

        if ((variable.playerX < -1) or (variable.playerX > 1)) and (variable.speed > variable.offRoadLimit):
            variable.speed = variable.speed = self.Util.accelerate(variable.speed, variable.offRoadDecelerate, variable.step)

        variable.playerX = self.Util.limit(variable.playerX, -2, 2)
        variable.speed = self.Util.limit(variable.speed, 0, variable.maxSpeed)

    # Builds up the array of our road at the beginning or if our road finishes
    def resetRoad(self, variable):
        for x in range(1, 501):
            if math.floor(x / variable.rumbleLength) % 2 == 0:
                variable.segments.append(Segment(x, variable, "dark"))
            else:
                variable.segments.append(Segment(x, variable, "light"))
        variable.trackLength = len(variable.segments) * variable.segmentLength