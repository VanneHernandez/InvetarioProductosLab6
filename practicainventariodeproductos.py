def consultar_inventario(inventario, producto):
    """Consulta la cantidad de un producto en el inventario."""
    if producto in inventario:
        return f"El producto '{producto}' tiene {inventario[producto]} unidades en inventario."
    else:
        return f"El producto '{producto}' no se encuentra en el inventario."

def agregar_producto(inventario, producto, cantidad):
    """Agrega un producto al inventario o incrementa su cantidad si ya existe."""
    if producto in inventario:
        inventario[producto] += cantidad
        return f"Se han agregado {cantidad} unidades del producto '{producto}'."
    else:
        inventario[producto] = cantidad
        return f"Producto '{producto}' agregado con {cantidad} unidades."

def eliminar_producto(inventario, producto):
    """Elimina un producto del inventario."""
    if producto in inventario:
        del inventario[producto]
        return f"El producto '{producto}' ha sido eliminado del inventario."
    else:
        return f"El producto '{producto}' no se encuentra en el inventario."

def mostrar_inventario(inventario):
    """Muestra el inventario completo de forma ordenada."""
    if not inventario:
        return "El inventario está vacío."
    inventario_ordenado = sorted(inventario.items())
    inventario_str = "\n".join([f"- {producto}: {cantidad}" for producto, cantidad in inventario_ordenado])
    return f"Inventario actual:\n{inventario_str}"

def main():
    # Inventario inicial
    inventario = {
        'manzanas': 50,
        'bananas': 30
    }

    # Mostrar inventario inicial
    print(mostrar_inventario(inventario))

    while True:
        # Menú de opciones
        print("\n¿Qué acción deseas realizar? (consultar/agregar/eliminar/mostrar/salir): ", end="")
        accion = input().strip().lower()

        if accion == 'salir':
            print("¡Gracias por usar el sistema de inventario!")
            break
        elif accion == 'consultar':
            producto = input("Ingresa el nombre del producto: ").strip().lower()
            print(consultar_inventario(inventario, producto))
        elif accion == 'agregar':
            producto = input("Ingresa el nombre del producto: ").strip().lower()
            cantidad = int(input("Ingresa la cantidad: "))
            print(agregar_producto(inventario, producto, cantidad))
            print(mostrar_inventario(inventario))
        elif accion == 'eliminar':
            producto = input("Ingresa el nombre del producto: ").strip().lower()
            print(eliminar_producto(inventario, producto))
            print(mostrar_inventario(inventario))
        elif accion == 'mostrar':
            print(mostrar_inventario(inventario))
        else:
            print("Acción no válida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    main()
