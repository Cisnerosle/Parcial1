# Crear una base de datos para almacenar detalles del producto y cantidad en stock
base_de_datos = {}

while True:
    print("¿Qué acción quieres realizar?")
    print("1. Ingresar un producto")
    print("2. Procesar una compra")
    print("3. Salir")
    opcion = int(input("Opción: "))
    if opcion == 1:
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: ")) 
        cantidad = float(input("Cantidad en stock: "))
        
        while cantidad!= int((cantidad*10)//10):
            print(f"No se puede vender {cantidad} de {nombre}")
            cantidad = float(input("Cantidad en stock: "))
        cantidad=int(cantidad*10)//10

        base_de_datos[nombre] = {'precio': precio, 'cantidad': cantidad}
    elif opcion == 2:
        total = 0
        lista_de_compras = []
        while True:
            nombre = input("Nombre del producto: ")
            if nombre not in base_de_datos:
                print("Lo sentimos, no tenemos este producto en nuestra tienda.")
            
            elif nombre in base_de_datos:
                cantidad = float(input("Cantidad: "))
            
                while cantidad!= int((cantidad*10)//10):
                    print(f"No se puede vender {cantidad} de {nombre}")
                    cantidad = float(input("Cantidad en stock: "))
                    cantidad=int(cantidad*10)//10

                if cantidad > base_de_datos[nombre]['cantidad']:
                    print("Lo sentimos, no tenemos suficiente stock de este producto.")
                
                elif cantidad <= 0:
                    print("La cantidad debe ser mayor que 0.")
                
                else:
                    lista_de_compras.append({'nombre': nombre, 'precio': base_de_datos[nombre]['precio'], 'cantidad': cantidad})
                    base_de_datos[nombre]['cantidad'] -= cantidad
                    exit = input("¿Quieres agregar otro producto? (s/n): ")

                    if exit.lower() == 'n':
                        break
        print("-----Resumen de compra-----")
        for producto in lista_de_compras:
            total += producto['precio'] * producto['cantidad']
            print(f"{producto['nombre']}: {producto['cantidad']} x {producto['precio']} = {producto['precio']*producto['cantidad']}")
        print(f"Total: {total}")
    elif opcion == 3:
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")



