class Animal:
    def __init__(self, cover, paws, tail, habitat, movement) -> None:
        self.cover = cover
        self.paws = paws
        self.tail = tail
        self.__habitat = habitat
        self.movement = movement

    def det_info (self):
        return self.__habitat
    def put_info (self, h):
        self.__habitat = h    

    def show_info (self):
            print (self.cover, self.paws, self.tail, self.__habitat, self.movement)