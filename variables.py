import pygame
import math

class Variable:

    def __init__(self):
        self.fps = 60
        self.step = 1.0/self.fps
        self.width = 1024
        self.height = 768
        self.fieldOfView = 100
        self.segments = []
        self.segmentLength = 200
        self.roadLength = 500
        self.roadWidth = 2000
        self.trees = pygame.image.load("images/background/trees.png")
        self.sky = pygame.image.load("images/background/sky.png")
        self.hills = pygame.image.load("images/background/hills.png")
        self.cameraHeight = 1000
        self.cameraDepth = 1 / math.tan((self.fieldOfView/2) * math.pi/180)
        self.currentFrame = 0
        self.distanceFromCameraToScreen = 0
        self.distanceFromCameraToCar = 0
        self.screenYCoordinate = 0
        self.deltaTime = 0
        self.LastFrame = 0
        self.gDeltaTime = 0
        self.position = 0
        self.speed = 0
        self.maxSpeed = self.segmentLength/self.step
        self.accelerate = self.maxSpeed/5
        self.breaking = -self.maxSpeed
        self.decelerate = -self.maxSpeed/5
        self.offRoadDecelerate = -self.maxSpeed/2
        self.offRoadLimit = self.maxSpeed/4
        self.trackLength = None
        self.rumbleLength = 3
        self.playerX = 0
        self.playerZ = self.cameraHeight * self.cameraDepth
        self.drawDistance = 300
        self.lanes = 3
