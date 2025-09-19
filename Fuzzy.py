import math

class Logicas:

    def Triangulho(self,x, a, b, c):
        if x <= a:
            return 0
        elif a < x < b:
            return (x - a) / (b - a)
        elif x == b:
            return 1
        elif b < x < c:
            return (c - x) / (c - b)
        elif x >= c:
            return 0

    def Trapezilho(self,x, a, b, c, d):
        if x <= a:
            return 0
        elif a < x <= b:
            return (x - a) / (b - a)
        elif b < x < c:
            return 1
        elif c <= x < d:
            return (d - x) / (d - c)
        elif x >= d:
            return 0

    def Gaussianadas(self,x, c, o):
        return math.exp(-((x - c) ** 2) / ((2 * o) ** 2))
    
