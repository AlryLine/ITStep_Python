from animal import Animal

class Artiodactyls (Animal):
    def __init__(self, cover, paws, tail, habitat, movement, presence_of_hooves, count_fingers_under_hooves) -> None:
        super().__init__(cover, paws, tail, habitat, movement)
        self.__presence_of_hooves = presence_of_hooves
        self.count_fingers_under_hooves = count_fingers_under_hooves
        
    def get_hooves (self):
        return self.__presence_of_hooves
    def put_hooves (self, hooves):
        self.__presence_of_hooves = hooves
        
                