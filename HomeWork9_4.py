class Car:
    def __init__(self):
        self.speed = 0
        self.color = 'Green'
        self.name = 'Mazda'
        self.is_police = False

    # методы класса
    def car_go(self, max_speed):
        self.speed = max_speed
        print(f"Автомобиль {self.name} разогнался до {self.speed} км/ч")

    def car_stop(self):
        self.speed = 0
        print(f"Автомобиль {self.name} остановился!")

    def turn(self, direction):
        if self.speed != 0:
            print(f"Автомобиль {self.name} повернул на {direction}!")
        else:
            print(f"Автомобиль {self.name} не может повернуть, он стоит")

    def show_speed(self):
        print(f"Автомобиль {self.name} разогнался до {self.speed}!")


class TownCar(Car):
    police_speed = 60

    def show_speed(self):
        if self.speed > self.police_speed:
            print(f"Автомобиль {self.name} разогнался до {self.speed}! Вас останавливает Полиция..."
                  f"Нарушаем... вы превысили скорость на {self.speed - self.police_speed} км/ч")
        else:
            print(f"Автомобиль {self.name} разогнался до {self.speed}!")


class SportCar(Car):
    police_speed = 200


class WorkCar(Car):
    police_speed = 40

    def show_speed(self):
        if self.speed > self.police_speed:
            print(f"Автомобиль {self.name} разогнался до {self.speed}! Вас останавливает Полиция..."
                  f"Нарушаем... вы превысили скорость на {self.speed - self.police_speed} км/ч")
        else:
            print(f"Автомобиль {self.name} разогнался до {self.speed}!")


class PoliceCar(Car):
    police_speed = 9999999999


b = TownCar()
b.car_go(50)
b.turn('направо')
b.car_go(60)
b.turn('налево')
b.car_go(70)
b.show_speed()
