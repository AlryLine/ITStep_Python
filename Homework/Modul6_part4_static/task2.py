class Temperature:
    count = 0
        
    @staticmethod
    def celsius_in_fahrenheit (celsius):
        Temperature.count += 1
        res = (celsius * 1.8) + 32
        return res
        
    @staticmethod
    def fahrenheit_in_celsius (fahrenheit):
        Temperature.count += 1
        res = (fahrenheit - 32) / 1.8
        return res
         
    @staticmethod
    def get_count ():
        return Temperature.count
    
f1 = Temperature.celsius_in_fahrenheit (24)
print ('З Цельсію в Фаренгейт:', f1)
f2 = Temperature.celsius_in_fahrenheit (-5) 
print ('З Цельсію в Фаренгейт:', f2)
c1 = Temperature.fahrenheit_in_celsius (95)
print ('З Фаренгейта в Цельсій:', c1)
c2 = Temperature.fahrenheit_in_celsius (45.5)
print ('З Фаренгейта в Цельсій:', c2)
print('Кількість підрахунків температури:', Temperature.get_count())