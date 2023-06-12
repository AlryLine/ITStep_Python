from animal import Animal
class Birds (Animal):
    def __init__(self, name, cover, paws, tail, habitat, movement, sound, wings, color_of_feathers, beak, egg_laying):
        super().__init__(name, cover, paws, tail, habitat, movement, sound)
        self.wings = wings
        self.color_of_feathers = color_of_feathers
        self.__beak = beak
        self.egg_laying = egg_laying

    def get_beak (self):
        return self.__beak
    def put_beak (self, beak):
        self.__beak = beak
      
    def __str__(self):                
        return f'Кількість лап: {self.paws}.'      

    def determine_color_of_feathers (self, color_of_feathers):
        if color_of_feathers == 'чорний':
            print ('Птах має пір\'я чорного кольору.')
        elif color_of_feathers == 'білий':
            print ('Птах має пір\'я білого кольору.')
        else:
            print ('Птах має пір\'я іншого кольору.')    

    def bird_fly (self, wings):
        if wings == 1:
            print ('Птах взлетів.')
        elif wings == 2:
            print ('Птах сів на гілку.')
            
    def sing_bird (self, sound):
        if sound == 'співай!':
            print ('Птах заспівав.')
        else:
            print ('Птах не співає.')                            
                 
    def show_info(self):
        super().show_info()
        
