class Book:
    def __init__ (self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.__author = author
        self.price = price
    
    def get_author (self):
        return self.__author
    def put_author (self, author):
        self.__author = author

    def print_message (self):
        print ('Увага! Книга з віковим обмеженням (18+)')

    def get_info (self):
        return (self.name, self.year, self.publisher, self.genre, self.__author, self.price)
    def show_info (self):
        print ('Маю для вас одну цікаву книгу!')

book = Book ('"Крейдяна людина"', 2018, 'книжковий клуб "Клуб сімейного дозвілля"', 'триллер', 5, 145)
book.show_info ()
book.put_author ('С. Дж. Тюдор')
print ('Назва:', book.name)
print ('Рік видання:', book.year)
print ('Видавництво:', book.publisher)
print ('Жанр:', book.genre)
print ('Автор:', book.get_author())
print ('Ціна:', book.price, 'грн')
book.print_message ()