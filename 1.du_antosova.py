#program pro hraní piškvorek na libovolně velké hrací ploše tvořené z šestiúhelníků. Velikost strany šestiúhelníku je 50 jednotek.
#uživatel zadává souřadnice od 1 do a (a = počet sloupců) a od 1 do b (b = počet řádků). Souřadnice [1,1] je v levém horním poli.

from turtle import forward, left, right, penup, pendown, speed, setpos, ycor, pensize, circle, exitonclick

sloupce = int(input("Zadejte počet sloupců:"))                                            #uživatel si zvolí velikost hrací plochy
radky = int(input("Zadejte počet řádků:"))

while sloupce <=0 or radky <=0:
    print("Chybný vstup, zadejte kladné číslo")
    sloupce = int(input("Zadejte počet sloupců:"))                                       
    radky = int(input("Zadejte počet řádků:"))      
       
speed(0)                                                                                  

pensize(5)                                                                                

left(30)                                                                                  #vykreslení šestiúhelníkové sítě
for i in range (radky):
    for i in range (sloupce):
        for i in range(8):
            forward(50)
            right(60)
        left(120)
    penup()
    setpos(0,ycor()-100)
    pendown() 
right(60)


pensize(2)                                                                                

pocitadlo = 0                                                                                            
while pocitadlo < (sloupce*radky):                                                        #program se ptá uživalů na souřadnice vykreslení symbolů do té doby, než zaplní hrací plochu
    pocitadlo +=1                                                                         
    
    if pocitadlo % 2 == 1:                                                                
        print("Nyní hraje hráč za křížky.")
        
        x = int(input("Zadejte souřadnici x: "))                                          
        
        if x <= 0 or x > sloupce:                                                          
            print("Byly zadány souřadnice mimo hrací pole, zadejte znovu.")
            pocitadlo -=1
            continue

        y = int(input("Zadejte souřadnici y: "))
        
        if y <= 0 or y > radky:
            print("Byly zadány souřadnice mimo hrací pole, zadejte znovu.")
            pocitadlo -=1
            continue
        penup()                                                                            #vykreslení křížku     
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
        print ("Nyní hraje hráč za kolečko.")                                              
        x = int(input("Zadejte souřadnici x: "))                                           
                                                                                                            
        if x <= 0 or x > sloupce:                                                                
            print("Byly zadány souřadnice mimo hrací pole, zadejte znovu.")
            pocitadlo -=1
            continue

        y = int(input("Zadejte souřadnici y: "))
        
        if y <= 0 or y > radky:
            print("Byly zadány souřadnice mimo hrací pole, zadejte znovu.")
            pocitadlo -=1
            continue 

        penup()                                                                             #vykreslení kolečka
        setpos((x-1)*86.6, (y-1)*(-100))
        right(39)
        forward(40)
        pendown()
        circle(30)
        left(39)

exitonclick()
