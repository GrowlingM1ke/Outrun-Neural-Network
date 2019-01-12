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

    def project(self, p, variable):
        p["camera"]["x"] = (p["world"]["x"] or 0) - variable.playerX * variable.roadWidth
        p["camera"]["y"] = (p["world"]["y"] or 0) - variable.cameraHeight
        p["camera"]["z"] = (p["world"]["z"] or 0) - variable.position
        p["screen"]["scale"] = variable.cameraDepth/p["camera"]["z"]
        p["screen"]["x"] = round((variable.width / 2) + (p["screen"]["scale"] * p["camera"]["x"] * variable.width / 2))
        p["screen"]["y"] = round((variable.height / 2) - (p["screen"]["scale"] * p["camera"]["y"] * variable.height / 2))
        p["screen"]["w"] = round((p["screen"]["scale"] * variable.roadWidth * variable.width / 2))
