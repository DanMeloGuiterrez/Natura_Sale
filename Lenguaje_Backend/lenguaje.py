import mysql.connector # pip install mysql-connector-python

# Connection information Aiven
conexion = mysql.connector.connect(
    host="natura-sale-base-datos-nature-sale.k.aivencloud.com",    
    user="avnadmin",      
    password="AVNS_0w9Ehs191pN4lT79WxM",
    database="defaultdb",
    port= "16992"
)

 
miCursor = conexion.cursor()  # Es lo que va a trabajar sobre la base de datos
 
# Reconoce mi base de datos
miCursor.execute("SHOW DATABASES") # devuelve una lista de todas las bases de datos disponibles
consulta = miCursor.fetchall() # me devuelve en una lista de tuplas
print(consulta)

# Funcion Insertar Datos
def ingresar_datos_producto():

    nombre_producto = input("Nombre Producto: ")
    precio = float(input("Precio: "))
    imagen = input("Imagen: ")
    descripcion = input("Descripcion: ")
    stock = int(input("Stock: "))
    print("\n1: Plantas Ornamentales")
    print("2: Frutales")
    print("3: Arboles")
    print("4: Suculentas")
    print("5: Enredaderas, plantas trepadoras y colgantes")
    print("6: Ventas de Herramientas y Macetas")
    print("7: Venta de Abono y Sustratos\n")
    id_categoria = int(input("id_categoria: "))

    # Indica que se va a insertar un nuevo registro en la tabla producto; %s : indicador 
    sql = "INSERT INTO producto(nombre_producto, precio, imagen, descripcion, stock, id_categoria) VALUES(%s, %s, %s, %s, %s, %s)"
    valores = (nombre_producto, precio, imagen, descripcion, stock, id_categoria)

    miCursor.execute(sql, valores)
    conexion.commit() #  confirmar los cambios 
    print("Registro guardado correctamente.")

def ingresar_datos_usuario():

    nombre_cliente = input("Nombre Cliente: ")
    apellido_cliente = input("Apellido Cliente: ")
    email = input("Email: ")
    contrasena = input("contraseña: ")
    telefono = int(input("telefono: "))
    direccion = input("direccion: ")
    dni = int(input("DNI: "))
    
    print("\n1: Usuario")
    print("2: Administrador\n")
    id_tipo_usuario = int(input("id_tipo_usuario: "))

    sql = "INSERT INTO usuario(nombre_cliente, apellido_cliente, email, contrasena, telefono, direccion, dni, id_tipo_usuario) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (nombre_cliente, apellido_cliente, email, contrasena, telefono, direccion, dni, id_tipo_usuario)

    miCursor.execute(sql, valores)
    conexion.commit()
    print("Registro guardado correctamente.")

# Funcion Mostrar Datos
def mostrar(tabla):
    sql = f"SELECT * FROM {tabla}"  # Selecciona la tabla producto
    miCursor.execute(sql)           # Se va a comunicar con la base 
    resultados = miCursor.fetchall()# Me devuevle todo los datos en forma de tuplas 

    for fila in resultados:         # Se imprime uno por uno 
        print(fila)

# Funcion Actualizar Datos
def actualizar_producto():
    #Le muestro la tabla producto
    print("\n")
    mostrar("producto")

    #Le pregunto que desea cambiar 
    id_producto = int(input("\nIngresa el ID del producto a actualizar: "))

    #Le muestro el producto
    print("Este es tu producto:")
    sql = "SELECT * FROM producto WHERE id_producto = %s"
    miCursor.execute(sql, (id_producto,))
    resultado = miCursor.fetchone() #Te devuelve una sola fila con los resultados 

    if resultado:
        print(resultado)
    else:
        print("Producto no encontrado.")
        return

    # Se escoge que modificar
    print("\n¿Qué campo deseas modificar?")
    print("- nombre_producto")
    print("- precio")
    print("- imagen")
    print("- descripcion")
    print("- stock")
    print("- id_categoria")
    campo = input("Campo a actualizar: ")
    nuevo_valor = input(f"Nuevo valor para {campo}: ")


    sql_update = f"UPDATE producto SET {campo} = %s WHERE id_producto = %s" # UPDATE producto SET {campo} = nuevo_valor WHERE id_producto = id_producto (1,2,3,..)
    miCursor.execute(sql_update, (nuevo_valor, id_producto)) # Manda la orden sql_update con los siguientes valores
    conexion.commit() #  confirmar los cambios 
    print("Producto actualizado")

def actualizar_usuario():

    print("\n")
    mostrar("usuario")

    id_usuario = int(input("Ingresa el ID del usuario a actualizar: "))

    print("Este es tu usuario:")
    sql = "SELECT * FROM usuario WHERE id_usuario = %s"
    miCursor.execute(sql, (id_usuario,))
    resultado = miCursor.fetchone()

    if resultado:
        print(resultado)
    else:
        print("Usuario no encontrado")
        return

    print("\n¿Que campo deseas modificar?")
    print("- nombre_cliente")
    print("- apellido_cliente")
    print("- email")
    print("- contrasena")
    print("- telefono")
    print("- direccion")
    print("- dni")
    print("- id_tipo_usuario")
    campo = input("Campo a actualizar: ")
    nuevo_valor = input(f"Nuevo valor para {campo}: ")

    sql_update = f"UPDATE usuario SET {campo} = %s WHERE id_usuario = %s"
    miCursor.execute(sql_update, (nuevo_valor, id_usuario))
    conexion.commit()
    print("Usuario actualizado")

# Funcion Eliminar Datos
def eliminar(entidada):
    id = int(input(f"Ingresa el ID del {entidada} a eliminar: "))
    sql = f"DELETE FROM {entidada} WHERE id_{entidada} = %s" # Se elimina de la tabla "entidad" el id_entidad (1,2,3,..)
    miCursor.execute(sql, (id,))
    conexion.commit() #  confirmar los cambios 
    print("ID eliminado")




# Mini Interface
print("\t Mini Interface \t")
print("\t 1: Insertar\t")
print("\t 2: Mostrar \t")
print("\t 3: Actualizar o Seleccionar\t")
print("\t 4: Eliminar \t")
eleccion_usuario = input("Elige una opcion: ")

# 1: Insertar
if eleccion_usuario == "1" or eleccion_usuario == "insertar":
    print("\n\t 1: Producto")
    print("\t 2: Usuario")
    eleccion_usuario_insertar = input("Elige una opcion: ")
    
    if eleccion_usuario_insertar == "1" or eleccion_usuario_insertar.lower()  == "producto":
        ingresar_datos_producto()
    elif eleccion_usuario_insertar == "2" or eleccion_usuario_insertar.lower()  == "usuario":
        ingresar_datos_usuario()
    else:
        print("Opcion de insercion no valida")


# 2: Mostrar
elif eleccion_usuario == "2" or eleccion_usuario == "mostrar":
    print("\n\t 1: Producto")
    print("\t 2: Usuario")
    eleccion_usuario_mostrar = input("Elige una opcion: ")

    if eleccion_usuario_mostrar == "1" or eleccion_usuario_mostrar.lower() == "producto":
        mostrar("producto")
    elif eleccion_usuario_mostrar == "2" or eleccion_usuario_mostrar.lower() == "usuario":
        mostrar("usuario")
    else:
        print("Opcion de mostrar no valida")


# 3: Actualizar o Seleccionar
elif eleccion_usuario == "3" or eleccion_usuario == "modificar" or eleccion_usuario == "seleccionar":
    print("\n\t 1: Producto")
    print("\t 2: Usuario")
    eleccion_usuario_actualizar = input("Elige una opcion: ")
    if eleccion_usuario_actualizar == "1" or eleccion_usuario_actualizar.lower() == "producto":
        actualizar_producto()
    elif eleccion_usuario_actualizar == "2" or eleccion_usuario_actualizar.lower() == "usuario":
        actualizar_usuario()
    else:
        print("Opcion de mostrar no valida")


# 4: Eliminar
elif eleccion_usuario == "4" or eleccion_usuario == "eliminar":
    print("\n\t 1: Producto")
    print("\t 2: Usuario")
    eleccion_usuario_eliminar = input("Elige una opcion: ")

    if eleccion_usuario_eliminar == "1" or eleccion_usuario_eliminar.lower() == "producto":
        print("\n Tablas de productos")
        mostrar("producto")
        print("\n")
        eliminar("producto")
    elif eleccion_usuario_eliminar == "2" or eleccion_usuario_eliminar.lower() == "usuario":
        print("\n Tablas de usuario")
        mostrar("usuario")
        print("\n")
        eliminar("usuario")
    else:
        print("Opcion de eleminar no valida")


# Caso en que no encuetre ninguno de los establecidos
else:
    print("Opcion principal no valida.")

miCursor.close() # Cierra ese vinculo con la base de datos
conexion.close() # Cierre ese logeo host con el Aiven 