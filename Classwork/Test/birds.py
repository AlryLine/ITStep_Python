from animal import Animal


class Birds (Animal):
    def __init__(self, cover, paws, tail, habitat, movement, wings, color_of_feathers, beak, sound) -> None:
        super().__init__(cover, paws, tail, habitat, movement)
        self.wings = wings
        self.color_of_feathers = color_of_feathers
        self.beak = beak
        self.sound = sound

    def determine_color_of_feathers (self, color_of_feathers):
        if color_of_feathers == 'чорний':
            print ('Птах має пір\'я чорного кольору.')
        elif color_of_feathers == 'білий':
            print ('Птах має пір\'я білого кольору.')

    def sing_of_bird (self, wings):
        if wings == 1:
            print ('Птах взлетів.')
        elif wings == 2:
            print ('Птах сів на гілку.')                
                 
    def show_info(self):
        super().show_info()
        print (self.wings, self.color_of_feathers, self.beak, self.sound)    