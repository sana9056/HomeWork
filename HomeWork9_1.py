import time


class TrafficLight:
    # атрибуты класса
    color_1 = 'краснный'
    color_2 = 'желтый'
    color_3 = 'зеленый'
    counter = 0

    # методы класса
    def running(self):
        print(f'TrafficLight is: {self.color_1}')
        time.sleep(7)
        print(f'TrafficLight is: {self.color_2}')
        time.sleep(2)
        print(f'TrafficLight is: {self.color_3}')
        time.sleep(3)


a = TrafficLight()
TrafficLight.running(a)
