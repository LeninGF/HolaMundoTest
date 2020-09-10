"""
Programa de Nomina de Empleados
"""

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

lista_empleados = [empleado_1, empleado_2, empleado_3]

# Imprimiendo empleados
for empleado in lista_empleados:
    nombre_empleado = empleado['nombre']
    salario_empleado = empleado['salario']
    print(nombre_empleado, salario_empleado)



