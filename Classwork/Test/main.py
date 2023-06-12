from animal import Animal
from mammals import Mammals
from birds import Birds
from artiodactyls import Artiodactyls

print ('Тварина - це царство переважно багатоклітинних еукаріотичних (ядерних) організмів,\nоднією з найголовніших ознак якого є гетеротрофність (тобто, споживання готових органічних речовин)\nта здатність активно рухатись.')
print ()

lioness = Mammals('Левиця.', 'Має вовну бежевого кольору.', 4, 'Має хвіст.', 'Живе в саваннах.', 'Передвигається лапами по землі.', 'Ричить.', 9)

lioness.put_lactation ('Годує молоком.')
print ('Вид:', lioness.name)
print ('Покрив:', lioness.cover)
print (str(lioness))
print ('Наявність хвоста:', lioness.tail)
print ('Середовище проживання:', lioness.habitat)
print ('Пересування:', lioness.movement)
print ('Звук:', lioness.sound)
print ('Особливості:', lioness.get_lactation ())
lioness.feed_cub ('Погодувати дитинча')
print ()

nightingale = Birds('Соловей.', 'Має пір\'я.', 2, 'Має хвіст.', 'Живе в лісі.', 'Передвигається в повітрі крилами.', 'Співає.', 'Має крила.', 'Має різні кольори пір\'я.', 11, 'Може нести яйця.')

nightingale.put_beak ('Має клюв.')
print ('Назва:', nightingale.name)
print ('Покрив:', nightingale.cover)
print (str(nightingale))
print ('Наявність хвоста:', nightingale.tail)
print ('Середовище проживання:', nightingale.habitat)
print ('Пересування:', nightingale.movement)
print ('Звук:', nightingale.sound)
print ('Наявність крил:', nightingale.wings)
print ('Колір пір\'я:', nightingale.color_of_feathers)
print ('Наявність клюва:', nightingale.get_beak ())
nightingale.determine_color_of_feathers ('сірий')
nightingale.bird_fly (1)
nightingale.sing_bird ('співай!')
print ()

deer = Artiodactyls('Олень.', 'Має вовну коричневого кольору.', 4, 'Має хвіст.', 'Живе в лісі.', 'Передвигається лапами по землі.', 'Реве.', 'Годує молоком.', 10, 'Має пальці.')

deer.put_hooves ('Має копита.')
print ('Назва:', deer.name)
print ('Покрив:', deer.cover)
print (str(deer))
print ('Наявність хвоста:', deer.tail)
print ('Середовище проживання:', deer.habitat)
print ('Пересування:', deer.movement)
print ('Звук:', deer.sound)
print ('Особливості:', deer.get_lactation())
print ('Наявність копит:', deer.get_hooves ())
print ('Наявність пальців під копитами:', deer.fingers)
deer.count_fingers (4)