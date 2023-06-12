from mammals import Mammals
class Artiodactyls (Mammals):
    def __init__(self, name, cover, paws, tail, habitat, movement, sound, lactation, hooves, fingers):
        super().__init__(name, cover, paws, tail, habitat, movement, sound, lactation)
        self.__hooves = hooves
        self.fingers = fingers
        
    def get_hooves (self):
        return self.__hooves
    def put_hooves (self, hooves):
        self.__hooves = hooves
        
    def __str__(self):                
        return f'Кількість лап: {self.paws}.'  
        
    def count_fingers (self, fingers):
        if fingers == 2 or fingers == 4:
            print ('Тварина парнокопитна.')
        elif fingers == 3 or fingers == 5:
            print ('Тварина непарнокопитна.')
            
    def show_info (self):
        super().show_info()
        print (self.__hooves, self.fingers)