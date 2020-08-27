ex  = [ pow ( 2 , 3 ), pow ( - 2 , 3 ),
                     pow ( 1 , 0 ),
                     pow (( - 1 ), 0 ),
                     pow ( 2 , 0 ),
                     pow (( 2 / 5 ), 3 ),
                     pow ( 3 , ( - 2 )),
                     pow (( 1 / 2 ), - 3 ),
                     pow ( - 1 , 3 ),
                     pow ( 0,5 , 3 ),
                     pow ( 0,25 , 4 ),
                     pow ( 0 , 4 ),
                     1  + ( pow ( 0,41 , 2 )),
                     ( 1 / 4 ) + ( pow ( 5 , 2 ) - ( pow ( 2 , - 4 ))),
                     ( pow ( 2 , - 3 ) + ( pow (( - 4 ), - 5 ))),
                     pow (( 4 / 5 ) - ( 1 / 2 ) +  1 , - 2 ) +  1  / ( 1  + ( pow ( 3 , 2 ) -  pow ( 4 - 5 , - 2 )))
                     ]
cont = 1
while(cont <= len(ex)):
    print(f'Exercicio {cont} = {ex[cont - 1]}')
    cont = cont + 1
