#program pro hraní piškvorek na libovolně velké hrací ploše tvořené z šestiúhelníků

from turtle import forward, left, right, penup, pendown, speed, setpos, ycor, pensize, circle

a = int(input("Zadejte počet sloupců:"))                                                  #uživatel si zvolí velikost hrací plochy
b = int(input("Zadejte počet řádků:"))

speed(0)                                                                                  #rychlost vykreslování

pensize(5)                                                                                #vykreslení mřížky pro přehlednost tlustší linií

left(30)                                                                                  #vykreslení šestiúhelníkové sítě
for i in range (b):
    for i in range (a):
        for i in range(8):
            forward(50)
            right(60)
        left(120)
    penup()
    setpos(0,ycor()-100)
    pendown() 
right(60)


pensize(2)                                                                                #vykreslení symbolů pro přehlednost užší linií

pocitadlo = 0                                                                                            
while pocitadlo < (a*b):                                                                  #program se ptá uživalů na souřadnice vykreslení symbolů do té doby, než zaplní hrací plochu
    pocitadlo +=1                                                                         #počítadlo úspěšného zadání souřadnic
    
    if pocitadlo % 2 == 1:                                                                #začíná hráč s křížky
        print("Nyní hraje hráč za křížky.")
        
        x = int(input("Zadejte souřadnici x: "))                                          #program se zeptá uživatele, kam si přeje zakreslit křížek
        
        if x <= 0 or x > a:                                                               #pokud uživatel zadá souřadnice mimo hrací plochu, program ho na to upozorní a nechá zadat znovu
            print("Byly zadány souřadnice mimo hrací pole, zadejte znovu.")
            pocitadlo -=1
            continue

        y = int(input("Zadejte souřadnici y: "))
        
        if y <= 0 or y > b:
            print("Byly zadány souřadnice mimo hrací pole, zadejte znovu.")
            pocitadlo -=1
            continue

        penup()                                                                           #vykreslení křížku     
        setpos((x-1)*86.6, (y-1)*(-100))
        pendown()
        forward(100)
        left(120)
        forward(50)
        left(120)
        forward(100)
        right(120)
        forward(50)
        right(120)
        
            
    else:
        print ("Nyní hraje hráč za kolečko.")                                              #jako druhý hraje hráč s kolečky
        x = int(input("Zadejte souřadnici x: "))                                           #program se zeptá uživatele, kam si přeje zakreslit kolečko
                                                                                                            
        if x <= 0 or x > a:                                                                #pokud uživatel zadá souřadnice mimo hrací plochu, program ho na to upozorní a nechá zadat znovu (while ciklus se spustí znovu)
            print("Byly zadány souřadnice mimo hrací pole, zadejte znovu.")
            pocitadlo -=1
            continue

        y = int(input("Zadejte souřadnici y: "))
        
        if y <= 0 or y > b:
            print("Byly zadány souřadnice mimo hrací pole, zadejte znovu.")
            pocitadlo -=1
            continue 

        penup()                                                                             #vykreslení křížku na uživalelem zvolenou pozici
        setpos((x-1)*86.6, (y-1)*(-100))
        right(39)
        forward(40)
        pendown()
        circle(30)

exitonclick()
