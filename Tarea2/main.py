import os
def Ej1_1_1():
    print(
        """\
    Ejemplo:
    
        P = {2, 3, 5, 7, 11, 13, …}
        AI = {rojo, naranja, amarillo, verde, azul, añil, violeta}
        """)
def Tema1_1_1():
    print(
        """
    1.1.1.  Definición formal de conjunto.
        
        Un conjunto, es una colección no ordenada y sin elementos repetidos. 
        Los usos básicos de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas.
        
        """)
    Ej1_1_1()
    

    

def Tema1_1_2():
    print(
        """
        1.1.2.  El conjunto universal y el conjunto vacío.
        
        Conjunto universal:  El conjunto universal es el conjunto formado 
        por todos los objetos de estudio en un contexto dado. Se denota por U.
        
        Conjunto vacío: El conjunto vacío es aquel que no tiene elementos.

        """)
    
def Tema1_1_3():
    print(
        """
        1.1.3. Definición de conjuntos por extensión y por comprensión.
        
        Conjuntos por extensión: Un conjunto está definido por extensión, 
        si se enumeran sus elementos.
        
        Conjunto por comprensión: Un conjunto se determina por comprensión, 
        cuando se da una propiedad, que la cumplan todos los elementos del conjunto.

        """)
    
def Tema1_2():
    print(
        """
        1.2. Operaciones con conjuntos.
        
        Las operaciones con conjuntos nos permiten realizar operaciones sobre 
        los conjuntos para obtener otro conjunto.

        """)
    
def Tema1_2_1():
    print(
        """
        1.2.1. Igualdad de conjuntos.
        
        Decimos que dos o más conjuntos son iguales si dichos conjuntos tienen los mismos elementos. 
        Recuerda que para determinar la igualdad de conjuntos no importa el orden de sus elementos.

        """)
    
def Tema1_2_2():
    print(
        """
        1.2.2. Subconjunto y superconjuntos.
        
        Subconjunto: Conjunto de elementos que tienen las mismas características y que está incluido dentro de otro conjunto más amplio.
        
        Superconjunto: Un superconjunto es un conjunto que incluye todos los elementos (y posiblemente más) de otro conjunto.

        """)
    
def Tema1_2_3():
    print(
        """
        1.2.3. Unión, intersección, complemento, diferencia y diferencia simétrica.
        
        Unión: Es la operación que nos permite unir dos o más conjuntos para formar otro conjunto que contendrá a todos los elementos 
        que queremos unir, pero sin que se repitan.
        
        Intersección: Es la operación que nos permite formar un conjunto, sólo con los elementos comunes involucrados en la operación.
        
        Complemento: Es la operación que nos permite formar un conjunto con todos los elementos del conjunto de referencia o universal, 
        que no están en el conjunto.
        
        Diferencia: Es la operación que nos permite formar un conjunto, en donde de dos conjuntos el conjunto resultante es el que tendrá 
        todos los elementos que pertenecen al primero pero no al segundo.
        
        Diferencia simétrica: Es la operación que nos permite formar un conjunto, en donde de dos conjuntos el conjunto resultante es el 
        que tendrá todos los elementos que no sean comunes a ambos conjuntos.

        """)
    
def Tema1_3():
    print(
        """
        1.3. Funciones.
        
        La definición de función nos dice que dados dos conjuntos y una relación de A en B podremos hablar de función si y sólo si 
        cada uno de los elementos de A bajo una regla de correspondencia (relación) va a dar a uno y sólo uno de B.
        
        """)
    
def Tema1_3_1():
    print(
        """
        1.3.1. Producto cartesiano.
        
        El producto cartesiano de dos conjuntos es una operación, que resulta en otro conjunto, cuyos elementos son todos los 
        pares ordenados que pueden formarse de forma que el primer elemento del par ordenado pertenezca al primer conjunto y el 
        segundo elemento pertenezca al segundo conjunto.
        
        """)
    
def Tema1_3_2():
    print(
        """
        1.3.2. Relaciones.
        
        Si un elemento está en un conjunto, se dice que pertenece al conjunto y en este caso usamos el símbolo ∈ para mostrar esta relación.
        
        """)


def Menu():

    while True:
        print("--------- Menu de Temas ---------")
        print("1)  1.1.1.  Definición formal de conjunto.")
        print("2)  1.1.2.  El conjunto universal y el conjunto vacío.")
        print("3)  1.1.3.  Definición de conjuntos por extensión y por comprensión.")
        print("4)  1.2.    Operaciones con conjuntos.")
        print("5)  1.2.1.  lgualdad de conjuntos.")
        print("6)  1.2.2.  Subconjunto y superconjunto.")
        print("7)  1.2.3.  Unión, Intersección, complemento, diferencia y diferencia simétrica.")
        print("8)  1.3.    Funciones.")
        print("9)  1.3.1.  Producto cartesiano.")
        print("10) 1.3.2.  Relaciones.")
        print("11) SALIR.")
        
        try:
            opc = int(input("Selecciona Opcion: "))
        except ValueError:
            Menu()
            
            
        if opc == 1:
            os.system("clear")
            Tema1_1_1()
        if opc == 2:
            Tema1_1_2()
        if opc == 3:
            Tema1_1_3()
        if opc == 4:
            Tema1_2()
        if opc == 5:
            Tema1_2_1()
        if opc == 6:
            Tema1_2_2()
        if opc == 7:
            Tema1_2_3()
        if opc == 8:
            Tema1_3()
        if opc == 9:
            Tema1_3_1()
        if opc == 10:
            Tema1_3_2()
        if opc == 11:
            break
            
        input("Presiona Enter para volver al menu   ")
        os.system('clear')

os.system('clear')
print("Tarea 2: Definiciones y Conjuntos.")
print("Argenis Jose Cuellar Medina 20110193")
Menu()