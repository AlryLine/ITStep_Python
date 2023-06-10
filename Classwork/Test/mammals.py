from animal import Animal

class Mammals (Animal):
    def __init__(self, cover, paws, tail, habitat, movement, lactation) -> None:
        super().__init__(cover, paws, tail, habitat, movement)
        self.lactation = lactation
        
    def get_movement (self):
        return self.__movement
    def put_movement (self, move):
        self.__movement = move
        
    def feed_cub (self, lactation):
        if lactation == 'Погодувати дитинча':
            print ('Годує дитинча.')
        if lactation == 'Перестати годувати':
            print ('Закінчує годування.')
            
    def show_info(self):
        super().show_info()
        print (self.lactation)         