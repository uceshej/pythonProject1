from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_point(self, x, y, kind=None):
        if kind == "Outside":
            plt.plot(x, y, "ro", label='Outside')
        elif kind == "Boundary":
            plt.plot(x, y, "bo", label='Boundary')
        elif kind == "Inside":
            plt.plot(x, y, "go", label='Inside')
        else:
            plt.plot(x, y, "ko", label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys())
        plt.show()


class Geometry:
    def __init__(self, id):
        self.__id = id

    def get_id(self):
        return self.__id


class Point(Geometry):
    def __init__(self, id, x, y, location='none'):
        Geometry.__init__(self, id)
        self.__x = x
        self.__y = y
        self.location = location

    def get_x(self):
        return float(self.__x)

    def get_y(self):
        return float(self.__y)

    def get_location(self):
        return self.location


class Line(Geometry):
    def __init__(self, id, point_1, point_2):
        Geometry.__init__(self, id)
        self.__point_1 = point_1
        self.__point_2 = point_2

    def get_point_1(self):
        return self.__point_1

    def get_point_2(self):
        return self.__point_2


class Polygon(Geometry):
    def __init__(self, id, points, xmax=0.0, xmin=0.0, ymax=0.0, ymin=0.0):
        Geometry.__init__(self, id)
        self.__points = points
        self.__xmax = xmax
        self.__xmin = xmin
        self.__ymax = ymax
        self.__ymin = ymin

    def lines(self):
        res = []
        points = self.get_points()
        point_a = points[0]
        for point_b in points[1:]:
            res.append(Line(point_a.get_id() + "-" + point_b.get_id(), point_a, point_b))
            point_a = point_b
        res.append(Line(point_a.get_id() + "-" + points[0].get_id(), point_a, points[0]))
        return res

    def get_points(self):
        return self.__points

    def get_xmax(self):
        return self.__xmax

    def get_xmin(self):
        return self.__xmin

    def get_ymax(self):
        return self.__ymax

    def get_ymin(self):
        return self.__ymin

    def get_MBR(self):
        points = self.get_points()
        for point in points:
            if point.get_x() > self.get_xmax():
                self.__xmax = point.get_x()
            if point.get_x() < self.get_xmin():
                self.__xmin = point.get_x()
            if point.get_y() > self.get_ymax():
                self.__ymax = point.get_y()
            if point.get_y() < self.get_ymin():
                self.__ymin = point.get_y()


class FileManager:

    # read the points of polygon and store them in a list
    def ReadPolygonPoint(self, filename, PolygonPoints=[]):
        self.filename = filename
        self.PolygonPoints = PolygonPoints
        with open(self.filename, 'r') as polyfile:
            lines = polyfile.readlines()[1:]
            for line in lines:
                temp = line.strip().split(',')
                pointsId = temp[0]
                pointsX = float(temp[1])
                pointsY = float(temp[2])
                pointsTemp = Point(pointsId, pointsX, pointsY)
                self.PolygonPoints.append(pointsTemp)
        return PolygonPoints

    # read the points to be categorized and store them in a list
    def ReadCheckPoint(self, filename, CheckPoints=[]):





