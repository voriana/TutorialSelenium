def calcular_promedio(mat1,mat2,mat3):
    suma= int(mat1+mat2+mat3)
    promedio=suma/3
    return promedio

def devuelve_nota():
    if promedio>=6 and promedio <9:
        print("El alumno {} {} tienen un promedio de {} y esta Aprobado".format(nombre,apellido,promedio))
    elif promedio >=4 and promedio<6:
        print("El alumno {} {} tienen un promedio de {} y va a recuperatorio".format(nombre,apellido,promedio))
    elif promedio< 4:
        print("El alumno {} {} tienen un promedio de {} y eta desaprobado".format(nombre,apellido,promedio))
    elif promedio>9:
        print("El alumno {} {} tienen un promedio de {} y esta Aprobado como alumno destacado".format(nombre,apellido,promedio))



if __name__ == '__main__':
    nombre= input("Ingrese el nombre del Alumno\n")
    apellido=input("Ingrese el Apellido\n")

    

    nota1= int(input("Ingrese la nota de Literatura: "))
    nota2= int(input("Ingrese la nota de Matematica: "))
    nota3= int(input("Ingrese la nota de fisica: "))

    promedio=calcular_promedio(nota1,nota2,nota3)
    devuelve_nota()

    


