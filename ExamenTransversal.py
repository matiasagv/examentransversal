import os
os.system ("cls")
Menu = """
1. Comprar Entradas.
2. Mostrar ubicaciones disponibles
3. Ver listado disponibles
4. Mostrar ganancias totales
5. Salir
"""
Entradas = """
1. Platinum           $120.000 (Asientos del 1 al 20)
2. Gold               $80.000  (Asientos del 21 al 50)
3. Silver             $50.000  (Asientos del 51 al 100)
"""
MenuUbicaciones = """
------------------------------------
          ESCENARIO
------------------------------------
1   2  3  4  5  6  7  8  9 10
11 12 13  x  x  x 17 18 19 20
21 22 23 24 25 26 27 28 29 30
31 32  x 34 35 36 37 38 39 40
41 42 43 44  x 46 47 48 49 50
51 52 53 54 55 56 57 58 59 60
61 62 63 64 65 66 67 68 69 70
71 72 73 74 75 76 77 78 79 80
81 82 83 84 85 86 87 88 89 90
91 92 93 94 95 96 97 98 99 100
"""
MenuRun = """
Los asistentes de este evento son
Juanito Casimiro 20451939
Michell Orleans  19843123

"""

nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
rut = input("Ingrese su rut: ")
RunVip = [20451939,198443123]
TotEntrada = 0
entrada = 0
def entradas():
    while True:
        try:
            entrada = int(input(Entradas))
            TotEntrada = int(input("¿Cuantas entradas desea?"))
            if entrada == 1:
             cPlat =+ 1
             entrada = cPlat * 120000
             break
            elif entrada == 2:
             cGold =+ 1
             entrada = cGold * 80000
             break
            elif entrada == 3:
             cSilver =+ 1
             entrada = cSilver * 50000
             break
            else:
             print("Error de rango [1-3]")
        except:
            print("Se produjo una excepcion")   
    #Fin del while de comprar entradas
ubi = 0
def ubicacion():
    while True:
        try:
            int(input(MenuUbicaciones))
            ubicaciones = int (input("¿Que ubicacion desea?"))
            input ("Presione enter para confirmar")
            if ubicaciones > 0 and ubicaciones <= 100:
                break
            elif ubicaciones >= 14 and ubicaciones <= 16:
                print ("Ubicaciones vendidas, por favor, intente nuevamente")
            elif ubicaciones == 33 and ubicaciones == 45:
                print ("Ubicaciones vendidas, por favor intente nuevamente")
            else:
                print ("Error en rango [1-100]")
        except:
            print ("Ha ocurrido una excepcion")
    #Fin del while de mostrar ubicaciones
def lista():
    print ("NOMBRE | APELLIDO | RUN ")
    print ("-------|----------|-----")
conts = 0

def ganancias ():
    print (f"""
    TIPO ENTRADA     |  CANTIDAD  |  TOTAL  |
    -----------------|------------|---------|
    Platinum $120.000|  {TotEntrada}         |$ {entrada}      |
    Gold     $80.000 |  {TotEntrada}         |$ {entrada}      |
    Silver   $50.000 |  {TotEntrada}         |$ {entrada}      |
    TOTAL            |            |         |
    -----------------------------------------
    """)
while True:
    try:
        opc = int (input(Menu))
        if opc == 5:
            input (f"Gracias {nombre} {apellido}, que vuelva pronto,|Fecha|10/07/2023")
        elif opc == 1:
            entradas ()
        elif opc == 2:
            ubicacion ()
        elif opc == 3:
            lista()
        elif opc == 4:
            ganancias()
    except: 
        print ("Error de excepcion")




