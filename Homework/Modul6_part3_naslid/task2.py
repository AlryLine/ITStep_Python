class Ship:
    def __init__(self, name, type_of_ship, speed, displacement_tonnage):
        self.name = name
        self.type_of_ship = type_of_ship
        self.speed = speed
        self.__displacement_tonnage = displacement_tonnage
        
    def get_displacement_tonnage (self):
        return self.__displacement_tonnage
    def put_displacement_tonnage (self, dis_tonn):
        self.__displacement_tonnage = dis_tonn
        
    def show_info (self):
        print (self.name, self.type_of_ship, self.speed,  self.__displacement_tonnage, end= ' ')
        
class Frigate (Ship):
    def __init__(self, name, type_of_ship, speed, displacement_tonnage, battery):
        super().__init__(name, type_of_ship, speed, displacement_tonnage)
        self.battery = battery
        
    