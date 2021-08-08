from itertools import cycle
from time import sleep


class TrafficLight:
    traffic_colors = ('красный', 'желтый', 'зеленый')
    times = (7, 2, 4)

    def __init__(self, color):
        self.__color = color

    def running(self):
        waiting = cycle(self.traffic_colors)
        for i in waiting:
            if self.__color == i:
                print(i)
                sleep(self.times[self.traffic_colors.index(self.__color)])
                self.__color = next(waiting)


my_traffic = TrafficLight('красный')
print(my_traffic.running())
