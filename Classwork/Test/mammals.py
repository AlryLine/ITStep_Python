from animal import Animal
class Mammals (Animal):
    def __init__(self, name, cover, paws, tail, habitat, movement, sound, lactation):
        super().__init__(name, cover, paws, tail, habitat, movement, sound)
        self.__lactation = lactation
        
    def get_lactation (self):
        return self.__lactation
    def put_lactation (self, lactation):
        self.__lactation = lactation
        
    def __str__(self):                
        return f'Кількість лап: {self.paws}.'
        
    def feed_cub (self, lactation):
        if lactation == 'Погодувати дитинча':
            print ('Годує дитинча.')
        if lactation == 'Перестати годувати':
            print ('Закінчує годування.')
            
    def show_info(self):
        super().show_info()