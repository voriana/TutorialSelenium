autos={'Ford': 100000,'Chevrolet':120000,'Fiat':80000}
puertas={'2':50000,'4':65000,'5':78000}
color={'Blanco':10000,'Azul':20000,'Negro':30000}

def obtener_datos():
    nombre= input("Ingrese nombre del cliente:\n").title()
    apellido= input("Ingrese apellido del cliente:\n").title()
    nombre_completo=nombre+' '+apellido
    return nombre_completo

for i in range(2):
	precio=0
	usuario_datos=obtener_datos()

	auto=input("Ingrese marca de auto:\n").title()
	if auto in autos:
		precio+=(autos[auto])
		print(precio)
	else:
		print("marca invalida")

	color_auto=input("Ingrese color de auto:\n").title()
	if color_auto in color:
		precio+=(color[color_auto])
		print(precio)
	else:
		print('color invalido')

	cant_puertas=input("Ingrese cantidad de puertas:\n")
	if cant_puertas in puertas:
		precio+=(puertas[cant_puertas])
		print(precio)
	    
	else:
		print('cantidad de puertas invalidas')

	print('la compra del usuario {} es: '.format(usuario_datos),precio)

