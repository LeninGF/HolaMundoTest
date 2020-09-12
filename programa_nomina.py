"""
Programa de Nomina de Empleados
"""

# Funciones Programa

def imprimir_nomina(lista, nombre_nomina):
    """
    :param lista: es la lista a imprimir
    :param nombre_nomina: es el titulo a imprimir a consola
    :return: no devuelve nada
    """
    print("----------------------------------------------------------------------\n")
    print("\t\t\tNomina de {}\n".format(nombre_nomina))
    print("Nombre \t\tEdad\t\tTelefono\t\tSalario\t\tPuesto")
    print("----------------------------------------------------------------------\n")
    for empleado in lista:
        nombre_empleado = empleado['nombre']
        salario_empleado = empleado['salario']
        edad_empleado = empleado['edad']
        puesto_empleado = empleado['puesto']
        telefono_empleado = empleado['telefono']
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(nombre_empleado, edad_empleado, telefono_empleado, salario_empleado, puesto_empleado))
    print("----------------------------------------------------------------------\n")


def imprimir_mejor_empleado():
    print("El mejor empleado no existe")

def imprimir_empleado_segun_mayor_sueldo():
    pass


# Programa Principal

empleado_1 = {'nombre':'Lenin', 
              'edad': 35, 
              'telefono': '0992884077', 
              'salario': 1250.22,
              'puesto': 'rrhh'}

empleado_2 = {'nombre':'Silvi', 
              'edad': 35, 
              'telefono': '0992342347', 
              'salario': 13434.22,
              'puesto': 'gerente servicio'}

empleado_3 = {'nombre':'Diana', 
              'edad': 35, 
              'telefono': '09234342347', 
              'salario': 12534.22,
              'puesto': 'puestoXYZ'}

empleado_4 = {'nombre':'Richard Dawkins', 
              'edad': 63, 
              'telefono': '0662884077', 
              'salario': 2000.00,
              'puesto': 'AteoBiolgoEvolucionista'}

empleado_5 = {'nombre':'Deepak Chopra', 
              'edad': 63, 
              'telefono': '09945542347', 
              'salario': 134.55,
              'puesto': 'vendedorDeEngaños'}

empleado_6 = {'nombre':'Curt Wallander', 
              'edad': 35, 
              'telefono': '09234342347', 
              'salario': 12534.22,
              'puesto': 'Detective'}


lista_empleados = [empleado_1, empleado_2, empleado_3]
lista_desempleados = [empleado_4, empleado_5, empleado_6]
# Imprimiendo empleados
imprimir_nomina(lista=lista_empleados, nombre_nomina='Empleados')
# Imprimir los desempleados
imprimir_nomina(lista=lista_desempleados, nombre_nomina='Desempleados')

imprimir_mejor_empleado()
print("Fin Programa")


