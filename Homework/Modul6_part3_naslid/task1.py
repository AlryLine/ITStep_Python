class Device:
    def __init__(self, brand, material, purpose, dimensions, price):
        self.brand = brand
        self.material = material
        self.purpose = purpose
        self.dimensions = dimensions
        self.price = price
    
    def show_info (self):
        print (self.brand, self.material, self.purpose, self.dimensions, self.price, end= ' ')
        
class CoffeeMachine (Device):
    def __init__(self, brand, material, purpose, dimensions, price, control_type, making):
        super().__init__(brand, material, purpose, dimensions, price)
        self.control_type = control_type
        self.making = making
    
    def info_about_coffee_machine (self):
        print ('Інформація про кавомашину:')
       
    def __str__ (self):
        return f' Бренд: {self.brand}\n Матеріал: {self.material}\n Призначення: {self.purpose}\n Габарити: {self.dimensions}\n Ціна: {self.price} грн\n Тип управління: {self.control_type}'
 
    def print_text (self):
        print ('Приготування кави:')
    
    def making_coffee (self, making):
        if making == 1:
            print (' Готується еспрессо')
        elif making == 2:
            print (' Готується капучіно')
        elif making == 3:
            print (' Готується латте')
        else:
            print (' Такого номера в меню немає! Будь-ласка, оберіть кавовий напій та натисніть кнопку від 1 до 3!')              
        
    def show_info (self):
        super().show_info()
        print (self.control_type, self.making)

class Blender (Device):
    def __init__(self, brand, material, purpose, dimensions, price, count_of_speeds, milk, fruits):
        super().__init__(brand, material, purpose, dimensions, price)
        self.count_of_speeds = count_of_speeds
        self.milk = milk
        self.fruits = fruits
     
    def info_about_blender (self):
        print ('Інформація про блендер:')    
        
    def make_milk_shake (self, milk, fruits):
        print ('Готуємо молочний коктель:')
        print (' Додаємо', milk, 'в блендер')
        print (' Тепер додаємо', fruits)
        print (' Змішуємо все разом')
        print ('Молочний коктель готовий!')            

    def show_info (self):
        super().show_info()
        print (self.count_of_speeds)
        
class MeatGrinder (Device):
    def __init__(self, brand, material, purpose, dimensions, price, reverse):
        super().__init__(brand, material, purpose, dimensions, price)
        self.__reverse = reverse
        
    def get_info_about_reverse (self):
        return self.__reverse
    def put_info_about_reverse (self, reverse):
        self.__reverse = reverse
        
    def info_about_meat_grinder (self):
        print ('Інформація про м\'ясорубку:')    
        
    def show_info (self):
        super().show_info()
        print (self.__reverse)

coffee_machine = CoffeeMachine ('Philips','пластик','приготування кавових напоїв','43,3 х 24,6 x 37,1 cм',35999,'сенсорний.', 7)
coffee_machine.info_about_coffee_machine ()
print ((coffee_machine))
print ()
coffee_machine.print_text ()
coffee_machine.making_coffee (3)
print ()
blender = Blender (' Бренд: Tefal\n','Матеріал: метал та пластик\n','Призначення: подрібнення їжі та збивання напоїв\n','Габарити: 40,6 х 19,2 х 21,5 см\n','Ціна: 4299 грн\n','Кількість швидкостей: мультишвидкісний', 7, 8)
blender.info_about_blender ()
blender.show_info ()
print ()
blender.make_milk_shake ('молоко', 'банан та полуницю')
print ()
meat_grinder = MeatGrinder (' Бренд: Bosch\n','Матеріал: пластик\n','Призначення: подрібнення м\'яса\n','Габарити: 25 х 16 х 23 см\n','Ціна: 5859 грн, зі знижкою - 4699 грн (-20%)\n', 6)
meat_grinder.get_info_about_reverse ()
meat_grinder.put_info_about_reverse ('Наявність реверса: так.')
meat_grinder.get_info_about_reverse ()
meat_grinder.info_about_meat_grinder ()
meat_grinder.show_info ()