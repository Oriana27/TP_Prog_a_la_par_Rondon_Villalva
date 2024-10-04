from funciones import mostrar_menu, agregar_producto, realizar_venta, mostrar_inventario_menu_ppal
"""variable global: """
opcion = 0

"""bucle principal del menu de inicio. """
mostrar_menu(opcion)
while opcion != 4:

    opcion = int(input("Ingrese la opcion deseada (1, 2, 3 o 4): "))
    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        realizar_venta()
    elif opcion == 3:
        mostrar_inventario_menu_ppal()
    elif opcion == 4:
        print("Saliendo del sistema. ¡Gracias por usar Yoda's Snack!")
    else:
        print(f"Opción no valida. Sistema Terminado")
