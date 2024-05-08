# app.py
from flask import Flask
from flask_graphql import GraphQLView
import graphene
import json
# Definición de tipos GraphQL

class Producto(graphene.ObjectType):
    sku = graphene.String()
    nombre = graphene.String()
    precio = graphene.Float()
    marca = graphene.String()
    descripcion = graphene.String()

# Ruta al archivo JSON donde se guardarán los productos
PRODUCTOS_JSON_FILE = 'productos.json'

# Definición de mutaciones GraphQL para insertar un nuevo producto
class CrearProducto(graphene.Mutation):
    class Arguments:
        sku = graphene.String(required=True)
        nombre = graphene.String(required=True)
        precio = graphene.Float(required=True)
        marca = graphene.String(required=True)
        descripcion = graphene.String()

    producto = graphene.Field(Producto)

    def mutate(self, info, sku, nombre, precio, marca, descripcion=None):
        nuevo_producto = {
            'sku': sku,
            'nombre': nombre,
            'precio': precio,
            'marca': marca,
            'descripcion': descripcion
        }
        
        # Abrir el archivo JSON en modo de escritura
        with open(PRODUCTOS_JSON_FILE, 'a') as file:
            # Guardar el nuevo producto en el archivo JSON
            json.dump(nuevo_producto, file)
            file.write('\n')  # Añadir nueva línea para cada producto
        
        return CrearProducto(producto=nuevo_producto)
# Definición de consultas GraphQL
class Query(graphene.ObjectType):
    producto = graphene.Field(Producto)

    def resolve_producto(self, info):
        # Aquí puedes escribir la lógica para obtener un producto de tu base de datos o de donde sea que estén tus datos
        # Por ahora, simplemente retornamos un producto de ejemplo
        return Producto(sku="SKU001", nombre="Producto de ejemplo", precio=100.0, marca="Marca de ejemplo", descripcion="Descripción de ejemplo")

class Mutaciones(graphene.ObjectType):
    crear_producto = CrearProducto.Field()
# Configuración de la aplicación Flask
app = Flask(__name__)

# Configuración del esquema GraphQL
schema = graphene.Schema(query=Query, mutation=Mutaciones)

# Ruta para la vista GraphQL
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)

