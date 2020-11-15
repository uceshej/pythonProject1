import matplotlib.pyplot as plt
from plotter import Plotter
plotter = Plotter()

class Geography:
    def __init__(self,name):
        self.name=name
    def get_name(self):
        return self.name

class Point(Geography):
    def __init__(self,name,x,y,location='')
        super().__init__(name)
        self.__x=float(x)
        self.__y=float(y)
        self.location=location
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_location(self):
        return self.location



class Polygen(Geography):
    def __init__(self,name,points):
        super().__init__(name)
        self.__points=points

class Line(Geogarphy):
    def __init__(self,name,point1,point2):
        super().__init__(name)
        self.__point1=point1
        self.__point2=point2
    def get_point1(self):
        return self.__point1
    def get_

