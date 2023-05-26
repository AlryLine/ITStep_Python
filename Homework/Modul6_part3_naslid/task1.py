class Device:
    def __init__(self, brand, material, purpose, dimensions, price):
        self.brand = brand
        self.material = material
        self.purpose = purpose
        self.__dimensions = dimensions
        self.price = price

    def get_dimensions (self):
        return self.__dimensions
    def put_dimensions (self, dimen):
        self.__dimensions = dimen
    
    def show_info (self):
        print (self.brand, self.material, self.purpose, self.__dimensions, self.price, sep= ' ')

class Blender (Device):
    def __init__(self, brand, material, purpose, dimensions, price, overheat):
        super().__init__(brand, material, purpose, dimensions, price)
        self.overheat = overheat
        self.dimensions = dimensions

    def show_info(self):
        super().show_info()
        print(self.overheat)

blender = Blender ('Марка блендеру: Tefal,', 'Матеріал: метал та пластик,', 'Призначення: подрібнення їжі та збивання напоїв,', 4, 'Ціна: 4299 грн,', 'Переваги: захист двигуна від перегріву.')
blender.get_dimensions()
blender.put_dimensions ('Габарити: 40,6 х 19,2 х 21,5 см,')
blender.get_dimensions()
blender.show_info ()
    