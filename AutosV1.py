#Dado el problema anterior del concesionario de autos debemos modificarlo, teniendo en cuenta:

#1-Ya no sabemos cuantos clientes tendremos,
#2-Si el pedido no es uno de los autos en venta, entonces debe volver a preguntar hasta que si lo sea
#3-Lo mismo con la cantidad de puertas y los colores.
#4-Al final se pregunta si hay otro cliente o no, si hay otro cliente, entonces vuelve a preguntar todo.
#5-Si la cantidad de clientes fue:
#--5.1: 0 a 5 personas no hay descuento
#--5.2: 6 a 10 personas: hay un descuento del 10%
#--5.3: 11 a 50 personas: hay un descuento del 15%
#--5.4: Más de 50 personas: El descuento es del 18%
#6-Solo se va a mostrar que se vendió al final del programa


autos={'Ford': 100000,'Chevrolet':120000,'Fiat':80000}
cant_puertas={'2':50000,'4':65000,'5':78000}
colores_auto={'Blanco':10000,'Azul':20000,'Negro':30000}
precio=0
cant_clientes=0




def obtener_datos():
    nombre= input("Ingrese nombre del cliente:\n").title()
    apellido= input("Ingrese apellido del cliente:\n").title()
    nombre_completo=nombre+' '+apellido
    return nombre_completo

def obtener_comando():
    print('Que desea hacer:')
    print('[S] ingrese S si desea agregar un usuario')
    print('[N] ingrese N para salir del sistema')

    comando=input().upper()
    if comando=='S':
        agregar=True
        #cant_clientes+=1
    elif comando=='N':
        agregar=False
    else:
        print('Error')
    
    return agregar

def aplica_descuento(cant,price):
    precio=price
    if cant <=5:
        print('No hay descuento')
        #precio=price 
    elif cant>5 and cant<=10:
        precio=precio-(precio*0.10)
    elif cant>10 and cant<=50:
        precio= precio-(precio*0.15)
    elif cant >50:
        #esta opcion de aplicar directamente el 18%
        precio*=0.82
    return precio

precio=0
cant_clientes=0



#Que desea hacer el cliente
agregar_usuario=obtener_comando()

#No se cuantos clientes son
while agregar_usuario:
    #contador de cuantos clientes voy agregando a la compra
    cant_clientes+=1

    #Obtener datos del cliente
    usuario_datos=obtener_datos()

    #Detalles de compra (marca,color,cant_puer)
    marca=None
    while not marca or marca not in autos:
        marca=input('Ingrese marca de auto a comprar\n').title()
        if marca in autos:
           precio+=(autos[marca])
           #print(precio)


    color=None
    while not color or color not in colores_auto:
        color=input('Indique color del auto a comprar\n').title()
        if color in colores_auto:
            precio+=(colores_auto [color])
            #print(precio)

    puertas=None
    while not puertas or puertas not in cant_puertas:
        puertas=input('Indique cantidad de puertas del auto a comprar\n').title()
        if puertas in cant_puertas:
            precio+=(cant_puertas[puertas])
            #print(precio)

    #print('la compra del usuario es {}'.format(usuario_datos), precio)
    
    agregar_usuario=obtener_comando() 


print('La cantidad de clientes es: ',cant_clientes)
print('La cuenta total es de: ',precio)
descuento=aplica_descuento(cant_clientes,precio)
print('El descuento aplicado a {clientes} clientes, es de:'.format(clientes=cant_clientes),descuento)




        
        









