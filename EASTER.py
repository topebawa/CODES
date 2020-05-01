while True:
    year = eval(input("Enter a year between 1982 - 2048: "))
    if 1982 <= year <= 2048:
        
        a = year % 10
        b = year % 7
        c = year % 4
        d = year  * ((19 * a) + 24) % 30
        e = ((2 * d) + (4 * c) + (6 * d) + 5) % 7
        date = 22 + d + e

        if date < 31:
            print("The date of easter is March", date)
            continue
        else:
            print("The date of easter is April", +(date - 31))
            
    else:
        print("The year you input is not between range given")
        break
    
