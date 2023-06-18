class Metric_to_Imperial_converter:
    
    @staticmethod
    def meters_to_feet(meters):
        feet = meters * 3.28084
        return feet

    @staticmethod
    def feet_to_meters(feet):
        meters = feet / 3.28084
        return meters

    @staticmethod
    def kilometers_to_miles(kilometers):
        miles = kilometers / 1.60934
        return miles

    @staticmethod
    def miles_to_kilometers(miles):
        kilometers = miles * 1.60934
        return kilometers
    
feet = Metric_to_Imperial_converter.meters_to_feet (5)
print ('Метри в фути:', feet)
meters = Metric_to_Imperial_converter.feet_to_meters (50)
print ('Фути в метри:', meters)
miles = Metric_to_Imperial_converter.kilometers_to_miles (10)
print ('Кілометри в мілі:', miles)
kilometers = Metric_to_Imperial_converter.miles_to_kilometers (25)
print ('Мілі в кілометри:', kilometers)
