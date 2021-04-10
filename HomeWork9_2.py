class Road:
    # атрибуты класса
    # методы класса
    def __init__(self):
        self.__length = 1000
        self.__width = 3
        self.__mass = 25
        self.__thickness = 5
        weight = self.__length * self.__width * self.__mass * self.__thickness
        print(f"Масса асфальта: {weight}")


Road()
