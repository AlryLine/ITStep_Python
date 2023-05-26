class Animal:
    def __init__(self, cover, paws, tail) -> None:
        self.cover = cover
        self.paws = paws
        self.__tail = tail
   
    def show_info(self):
        print(self.cover, self.paws, self.__tail)

class Tiger(Animal):
    def __init__(self, cover, paws, tail, sound) -> None:
        super().__init__(cover, paws, tail)
        self.sound = sound
    
    def show_info(self):
        super().show_info()
        print(self.sound)
    

class Crocodile(Animal):
    def __init__(self, cover, paws, tail, habitat) -> None:
        super().__init__(cover, paws, tail)
        self.habitat = habitat

    def show_info(self):
        super().show_info()
        print(self.habitat)


class Kangaroo(Animal):
    def __init__(self, cover, paws, tail, movement) -> None:
        super().__init__(cover, paws, tail)
        self.movement = movement

    def show_info(self):
        super().show_info()
        print(self.movement)



tiger = Tiger('Помаранчева вовна в полоску,', 'чотири лапи,', 'має хвіст,', 'ричить.')
tiger.show_info ()
crocodile = Crocodile('Шкіра має луску,', 'чотири лапи,', 'має хвіст,', 'живе у воді, але може перебувати на суші недовго.')
crocodile.show_info ()
kangaroo = Kangaroo('Бежева вовна,', 'чотири лапи,', 'має хвіст,', 'стрибає на двох задніх лапах.')
kangaroo.show_info ()



# teacher = Teacher("Dmytro", 'Medvediev', 37, '+380688535681', 'QA')
# teacher.show_info()
# persona = Persona("Dmytro", 'Medvediev', 37, '+380688535681')
# persona.show_info()
# zav = zav_kaf("Dmytro", 'Medvediev', 37, '+380688535681', 'QA')
# zav.show_info()