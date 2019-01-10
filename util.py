class Util:

    def increase(self, start, increment, max):
        result = start + increment
        while result >= max:
            result -= max
        while result < 0:
            result += max
        return result

    def accelerate(self, v, accelerate, deltaTime):
        return v + (accelerate * deltaTime)

    def limit(self, value, minimum, maximum):
        return max(minimum, min(value, maximum))

    def project(self, p, cameraX, cameraY, cameraZ, cameraDepth, width, height, roadWidth):
        p["camera"]["x"] = (p["world"]["x"] or 0) - cameraX
        p["camera"]["y"] = (p["world"]["y"] or 0) - cameraX
        p["camera"]["z"] = (p["world"]["z"] or 0) - cameraX
        p["screen"]["scale"] = cameraDepth/p["camera"]["z"]
        p["screen"]["x"] = round((width / 2) + (p["screen"]["scale"] * p["camera"]["x"] * width / 2))
        p["screen"]["y"] = round((height / 2) - (p["screen"]["scale"] * p["camera"]["y"] * height / 2))
        p["screen"]["w"] = round((p["screen"]["scale"] * roadWidth * width / 2))
