import os
from modelos.producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    # ================================
    # Cargar productos desde archivo
    # ================================
    def cargar_desde_archivo(self):
        try:
            # Si no existe el archivo, lo crea vacío
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()

            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        codigo, nombre, cantidad, precio = datos
                        producto = Producto(codigo, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)

            print("✔ Inventario cargado correctamente.")

        except FileNotFoundError:
            print("❌ Error: Archivo no encontrado.")
        except PermissionError:
            print("❌ Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print("❌ Error al cargar el archivo:", e)

    # ================================
    # Guardar en archivo
    # ================================
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos:
                    file.write(f"{producto.codigo},{producto.nombre},{producto.cantidad},{producto.precio}\n")

            print("✔ Cambios guardados en el archivo.")

        except PermissionError:
            print("❌ Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print("❌ Error al guardar el archivo:", e)

    # ================================
    # Añadir producto
    # ================================
    def añadir_producto(self, codigo, nombre, cantidad, precio):
        for producto in self.productos:
            if producto.codigo == codigo:
                print("❌ El producto ya existe.")
                return

        nuevo_producto = Producto(codigo, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        self.guardar_en_archivo()
        print("✔ Producto añadido correctamente.")

    # ================================
    # Eliminar producto
    # ================================
    def eliminar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                self.productos.remove(producto)
                self.guardar_en_archivo()
                print("✔ Producto eliminado correctamente.")
                return

        print("❌ Producto no encontrado.")

    # ================================
    # Mostrar productos
    # ================================
    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for producto in self.productos:
                print(f"Código: {producto.codigo} | Nombre: {producto.nombre} | Cantidad: {producto.cantidad} | Precio: {producto.precio}")