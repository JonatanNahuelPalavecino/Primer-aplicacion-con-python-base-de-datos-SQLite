import sqlite3

db = sqlite3.connect("ejemplo_bdd")

cur = db.cursor()

# FUNCIONES

def ver_tablas ():
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
        tablas = cur.fetchall()

        print("\nTABLAS\n")

        for tabla in tablas:
            print(tabla[0])

def ver_registros (dato):
    cur.execute(f"SELECT * FROM {dato}")
    registros = cur.fetchall()

    for registro in registros:
        print(registro)
        print("----------------------------------------") 

def crear_registro (tabla, dato_uno, dato_dos, dato_tres, dato_cuatro = 0):
    if tabla == "clientes":
        cur.execute("BEGIN;")
        cur.execute(f"INSERT INTO {tabla} VALUES ('{dato_uno}', '{dato_dos}', '{dato_tres}', '{dato_cuatro}');")
        cur.execute("COMMIT;")
    elif tabla == "ordenes":
        cur.execute("BEGIN;")
        cur.execute(f"INSERT INTO {tabla} VALUES ('{dato_uno}', '{dato_dos}', '{dato_tres}');")
        cur.execute("COMMIT;")
    else:
        return       
    
def modificar_registro (key, tabla, dato_uno, dato_dos, dato_tres = 0):
    if tabla == "clientes":
        cur.execute("BEGIN;")
        cur.execute(f"UPDATE {tabla} SET nombre = '{dato_uno}' WHERE id = '{key}';")
        cur.execute(f"UPDATE {tabla} SET apellido = '{dato_dos}' WHERE id = '{key}';")
        cur.execute(f"UPDATE {tabla} SET dni = '{dato_tres}' WHERE id = '{key}';")
        cur.execute("COMMIT;")
    elif tabla == "ordenes":
        cur.execute("BEGIN;")
        cur.execute(f"UPDATE {tabla} SET fecha = '{dato_uno}' WHERE orden_numero = '{key}';")
        cur.execute(f"UPDATE {tabla} SET id_cliente = '{dato_dos}' WHERE orden_numero = '{key}';")
        cur.execute("COMMIT;")
    else:
        return

def eliminar_registro (tabla, key):
    if tabla == "clientes":
        cur.execute("BEGIN;")
        cur.execute(f"DELETE FROM {tabla} WHERE id = '{key}';")
        cur.execute("COMMIT;")
    elif tabla == "ordenes":
        cur.execute("BEGIN;")
        cur.execute(f"DELETE FROM {tabla} WHERE orden_numero = '{key}';")
        cur.execute("COMMIT;")
    else:
        return

# COMIENZA LA APLICACION              

print("Bienvenido al programa de tu base de datos.")

opcion_general = 0

while opcion_general == 0:

    opcion = int(input("Ingrese el N° de la opcion que desea ejecutar:\n1) VER LAS TABLAS\n2) CREAR UN REGISTRO\n3) MODIFICAR UN REGISTRO\n4) ELIMINAR UN REGISTRO\n5) FINALIZAR\n"))

    if opcion == 1:

        ver_tablas ()

        tabla_elegida = input("\nEscriba el nombre de la tabla que desea visualizar: ")

        ver_registros(tabla_elegida)

        opcion_general = int(input("\n0) PARA VOLVER A LA PAGINA PRINCIPAL\n1) PARA FINALIZAR\n"))

    elif opcion == 2:
         
        ver_tablas ()

        tabla_elegida = input("\nEscriba la tabla a la que desea agregar un registro: ")

        if tabla_elegida == "clientes":
             
            id_nuevo = input("Ingrese el ID: ")
            nombre_nuevo = input("Ingrese el nombre: ")
            apellido_nuevo = input("Ingrese el apellido: ")
            dni_nuevo = input("Ingrese el DNI: ")
            crear_registro(tabla_elegida, id_nuevo, nombre_nuevo, apellido_nuevo, dni_nuevo)

        elif tabla_elegida == "ordenes":

            num_orden_nuevo = input("Ingrese el N° de orden: ")
            fecha_orden_nuevo = input("Ingrese la fecha de la orden del modo AÑO-MES-DIA: ")
            cliente_id_nuevo = input("Ingrese el N° de ID del cliente que solicitó la orden: ")
            crear_registro(tabla_elegida, num_orden_nuevo, fecha_orden_nuevo, cliente_id_nuevo)

        else:
            print("Elegiste una tabla que no existe.")

        opcion_general = int(input("\n0) PARA VOLVER A LA PAGINA PRINCIPAL\n1) PARA FINALIZAR\n"))        

    elif opcion == 3:

        ver_tablas ()

        tabla_elegida = input("\nEscriba la tabla de la que desea modificar un registro: ")        

        ver_registros(tabla_elegida)

        if tabla_elegida == "clientes":
            registro_elegido = input("Escriba el N° de ID del cliente que desea modificar: ")

            print("ATENCION: El campo ID del cliente no podrá ser modificado.")
            nombre_nuevo = input("Ingrese el nombre: ")
            apellido_nuevo = input("Ingrese el apellido: ")
            dni_nuevo = input("Ingrese el DNI: ")
            modificar_registro(registro_elegido, tabla_elegida, nombre_nuevo, apellido_nuevo, dni_nuevo)

        elif tabla_elegida == "ordenes":
            registro_elegido = input("Escriba el N° de Orden que desea modificar: ")

            print("ATENCION: El campo orden_numero no podrá ser modificado.")
            fecha_orden_nuevo = input("Ingrese la fecha de la orden del modo AÑO-MES-DIA: ")
            cliente_id_nuevo = input("Ingrese el N° de ID del cliente que solicitó la orden: ")
            modificar_registro(registro_elegido, tabla_elegida, fecha_orden_nuevo, cliente_id_nuevo)
        else:
            print("Elegiste una tabla que no existe.")

        opcion_general = int(input("\n0) PARA VOLVER A LA PAGINA PRINCIPAL\n1) PARA FINALIZAR\n")) 

    elif opcion == 4:

        ver_tablas ()

        tabla_elegida = input("\nEscriba la tabla de la que desea eliminar un registro: ")        

        ver_registros(tabla_elegida)

        if tabla_elegida == "clientes":
            registro_elegido = input("Escriba el N° de ID del cliente que desea eliminar: ")

            eliminar_registro(tabla_elegida, registro_elegido)            

        elif tabla_elegida == "ordenes":
            registro_elegido = input("Escriba el N° de Orden que desea eliminar: ")

            eliminar_registro(tabla_elegida, registro_elegido)

        else:
            print("Elegiste una tabla que no existe.")

        opcion_general = int(input("\n0) PARA VOLVER A LA PAGINA PRINCIPAL\n1) PARA FINALIZAR\n")) 

    elif opcion == 5:
        break
    else:
        print("Elegiste una tabla que no existe.")