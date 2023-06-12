class Animal:
    def __init__(self, name, cover, paws, tail, habitat, movement, sound):
        self.name = name
        self.cover = cover
        self.paws = paws
        self.tail = tail
        self.habitat = habitat
        self.movement = movement
        self.sound = sound

    def get_habitat (self):
        return self.__habitat
    def put_habitat (self, habitat):
        self.__habitat = habitat
        
    def __str__(self):                
        return f'Кількість лап: {self.paws}.'

    def show_info (self):
            print (self.name, self.cover, self.paws, self.tail, self.habitat, self.movement, self.sound)