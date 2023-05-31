class Wheels:
    def __init__(self, radius, width, type_of_tires, tires) -> None:
        self.radius = radius
        self.width = width
        self.type_of_tires = type_of_tires
        self.tires = tires

    def show_info (self):
        print ('Радіус колес: ', self.radius, 'Ширина колес: ', self.width, 'Тип гуми на колесах: ', self.type_of_tires)

    def change_tires (self, types_of_tires):
        if types_of_tires == 'w':  
            print ('Замінено з літьної гуми на зимню.')
        elif types_of_tires == 's':
            print ('Замінено з зимньої гуми на літню')
       
class Engine:
    def __init__(self, count_of_cylinders, power, type_of_fuel, type_of_engine) -> None:
        self.count_of_cylinders = count_of_cylinders
        self.power = power
        self.type_of_fuel = type_of_fuel
        self.type_of_engine = type_of_engine

    def show_info (self):
        print ('Кількість циліндрів: ', self.count_of_cylinders, 'Потужність двигуна: ', self.power, 'Тип палива: ', self.type_of_fuel, 'Тип двигуна: ', self.type_of_engine)

    def start_the_engine (self):
        print ('Двигун заведений!')   

class Doors:
    def __init__(self, door_handle, power_window, windows, height, type_lock, count_of_doors, doors) -> None:
        self.door_handle = door_handle
        self.power_window = power_window
        self.windows = windows
        self.height = height
        self.type_lock = type_lock
        self.count_of_doors = count_of_doors
        self.doors = doors

    def show_info (self):
        print ('Кількість дверник ручок: ', self.door_handle, 'Наявність склопід\'йомника: ', self.power_window, 'Наявність вікон: ', self.windows, 'Висота дверей: ', self.height, 'Тип замка: ', self.type_lock, 'Кількість дверей: ', self.count_of_doors, 'Наявність дверей: ', self.doors)

    def close_or_open_door (self, doors):
        if doors == 0:
            print ('Двері зачинені.')
        elif doors == 1:
            print ('Двері відчинені.')        

class Car (Wheels, Engine, Doors):
    def __init__(self, radius, width, type_of_tires, count_of_cylinders, power, type_of_fuel, type_of_engine, door_handle, power_window, windows, height, type_lock, count_of_doors, doors, color, model) -> None:
        Wheels().__init__(radius, width, type_of_tires)
        Engine().__init__(count_of_cylinders, power, type_of_fuel, type_of_engine)
        Doors().__init__(door_handle, power_window, windows, height, type_lock, count_of_doors, doors)
        self.color = color
        self.model = model

    def show_info(self):
        Wheels.show_info(self)
        Engine.show_info(self)
        Doors.show_info(self)
        print ('Модель авто: ', self.model, 'Колір авто: ', self.color, '')

