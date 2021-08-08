class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def info(self):
        print(f'Это {self.name} {self.color} цвета, {"полицейская" if self.is_police==True else "не полицейская"}')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)

    def show_speed(self):
        print('Текущая скорость автомобиля:', self.speed)


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)

    def show_speed(self):
        print('Текущая скорость автомобиля: ', self.speed)
        if self.speed > 60:
            print(f'Внимание! Превышение скорости на {self.speed-60}. Сбросьте скорость.')


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)

    def show_speed(self):
        print('Текущая скорость автомобиля: ', self.speed)
        if self.speed > 40:
            print(f'Внимание! Превышение скорости на {self.speed-40}. Сбросьте скорость.')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=True)


town_car = TownCar(71, 'красного', "Toyota")
town_car.info()
town_car.go()
town_car.turn("направо")
town_car.stop()
town_car.show_speed()

sport_car = SportCar(240, 'черного', "Aston Martin")
sport_car.info()
sport_car.go()
sport_car.turn("налево")
sport_car.stop()
sport_car.show_speed()

work_car = WorkCar(64, 'белого', 'Volvo')
work_car.info()
work_car.go()
work_car.turn("дважды налево")
work_car.stop()
work_car.show_speed()

police_car = PoliceCar(82, 'бело-синего', 'Audi')
police_car.info()
police_car.go()
police_car.turn("направо")
police_car.stop()
police_car.show_speed()
