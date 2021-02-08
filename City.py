
import math
# city class description where we will hold information about each city
destinations = []
class City:
    def __init__(self,x,y,name):
        self.x=x #coordinates
        self.y=y 
        self.name=name
    def getDistance(self , city):
        difX = self.x-city.x
        difY = self.y-city.y
        distance = math.sqrt(math.pow(difX,2)+math.pow(difY,2))
        return distance
    
    
"""def main():
    
    c1=City(2,5)
    c2=City(3,4)
    dist=c1.getDistance(c2)
    print(dist)"""
    