# . Menú principal:
# • Mostrar las siguientes opciones:
# o Agregar producto al inventario.
# o Realizar una venta.
# o Mostrar productos disponibles.
# o Salir del sistema


def mostrar_menu(menu) -> str:
    """Esta funcion muestra el menu principal, y se puede utilizar e
    dentro de otras funciones en el flujo de codigo.
    Argumentos: menu >> string
    Retornos: string
    """

    print(""" Bienvenido al sistema de Gestion del quiosco Yoda's Snack.
    Menu Principal:
    1) Agregar producto al inventario
    2) Realizar una venta
    3) Mostrar productos disponibles
    4) Salir del Sistema.
    """)
    return menu

# 2. Agregar producto al inventario:
# • Permitir al usuario agregar productos al inventario. Cada producto debe tener
# un nombre, una cantidad disponible y un precio unitario.
# • Los productos deben almacenarse en una lista.
# • Ver la estructura del inventario al final de la consigna


"""Aqui inicializamos una lista vacia para guardar los productos
que el usuario desee."""
inventario = []


def agregar_producto() -> list:
    """Esta funcion incluye un bucle while para que el usuario ingrese
    los datos de los productos, sin limite de ingresos.
    Argumentos: nombre_producto >> str
                cantidad >> int
                precio >> float
    Retornos: --
    """
    continuar = True
    while continuar:
        print(">>>>Agregar productos>>>> ")
        nombre_producto = input("Ingrese nombre del producto: ")
        cantidad = int(input("Ingrese cantidad de producto: "))
        precio = float(input("Ingrese precio del producto: "))

        """iniciamos una nueva lista con los datos ingresados, y los agregamos
        a la lista inicial inventario."""
        producto = [nombre_producto, cantidad, precio]
        inventario.append(producto)
        print(f"Producto '{nombre_producto}' agregado al inventario.")

        continuar = input("agregar mas productos? (si/no): ")
        if continuar == "no":
            continuar = False
            mostrar_menu(opcion)

# 3. Realizar una venta:
# • Mostrar una lista de productos disponibles (nombre, precio y cantidad).
# • El usuario podrá seleccionar un producto y la cantidad que desea comprar.
# • Verificar que haya suficiente stock del producto seleccionado.
# • Restar la cantidad comprada del inventario.
# • Mostrar el total a pagar al cliente por la venta.
# • Si no hay suficiente stock, mostrar un mensaje que indique que no se puede
# realizar la venta


def realizar_venta() -> float:
    """Esta funcion contiene otro bucle while para solicitar productos disponibles
    en el inventario, a su vez contiene bucle for para sumarlo a la venta y de misma 
    forma lo resta del inventario.
    Argumentos: nombre_producto >> str
                cantidad_venta >> int
    Retorno: -
    """
    mostrar_inventario()
    total_pagar = 0.0
    continuar = True
    while continuar:
        nombre_producto = input("Ingrese producto deseado: ")
        cantidad_venta = int(input("Ingrese cantidad deseada: "))
        for producto in inventario:
            if producto[0] == nombre_producto:
                if producto[1] >= cantidad_venta:
                    producto[1] -= cantidad_venta
                    total_pagar += producto[2] * cantidad_venta
                    print(f"Se restaron {cantidad_venta} unidades de {
                        nombre_producto}")
                else:
                    print("No hay suficiente stock para ralizar la venta")
                break
            else:
                print("Producto no encontrado en el inventario")
        print(f"Total a pagar: {total_pagar}")
        continuar = input("¿volver al menu anterior? (si/no) ")
        if continuar == "si":
            continuar = False
            mostrar_menu(opcion)


# 4. Mostrar productos disponibles:
# • Mostrar todos los productos en el inventario, con su nombre, cantidad
# disponible y precio.

def mostrar_inventario() -> list:
    """Esta funcion permite mostrar el inventario al momento de realizar
    una venta. 
    Argumentos: item de inventario >> list
    Return: list
    """
    print("Productos disponibles en el inventario:")
    for item in inventario:
        print(f"""Producto: {item[0]}
              Cantidad: {item[1]}
              Precio: {item[2]}""")
    return inventario


def mostrar_inventario_menu_ppal() -> list:
    """Esta funcion difiere de la anterior, esta funcion muestra el inventario
    desde el menu principal e incluye la opcion de volver
    al menu de inicio.
    Argumentos: item de inventario >> list
    Retronos: -
    """
    print("Productos disponibles en el inventario:")
    for item in inventario:
        print(f"""Producto: {item[0]}
              Cantidad: {item[1]}
              Precio: {item[2]}
        """)
    mostrar_menu(opcion)


"""esta variable global es necesario para las funciones, es un contador
que lo utilizamos en el bucle inicial luego de mostrar el menu principal 
con la funcion mostrar_menu."""
opcion = 0
