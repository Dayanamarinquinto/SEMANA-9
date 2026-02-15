# servicios/inventario.py
from modelos.producto import Producto
class Inventario:
    """
    Clase encargada de gestionar los productos.
    """

    def __init__(self):
        # Lista que almacena los productos
        self.productos = []

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto si el ID no está repetido.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: Ya existe un producto con ese ID.")
                return False

        self.productos.append(producto)
        print("✅ Producto añadido correctamente.")
        return True

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto por su ID.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("✅ Producto eliminado correctamente.")
                return True

        print("❌ Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """
        Actualiza cantidad y/o precio de un producto por ID.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                print("✅ Producto actualizado correctamente.")
                return True

        print("❌ Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por coincidencia parcial en el nombre.
        """
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)

        return resultados

    def mostrar_inventario(self):
        """
        Muestra todos los productos registrados.
        """
        if not self.productos:
            print("📦 El inventario está vacío.")
            return

        print("\n📋 Inventario actual:")
        for p in self.productos:
            print(p)