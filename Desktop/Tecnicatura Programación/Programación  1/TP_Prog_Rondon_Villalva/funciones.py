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
