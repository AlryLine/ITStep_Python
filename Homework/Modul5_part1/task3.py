def draw_square (side_lenght, symbol, fill = True):
    line_of_square = side_lenght * symbol
    if fill:
        for i in range (side_lenght):
            print(line_of_square)
            i += 1
    else:
        print (line_of_square)
        for i in range (side_lenght -2):
            print(symbol + ' ' * (side_lenght -2) + symbol)
        print (line_of_square)    
        
draw_square(6, '*', False)