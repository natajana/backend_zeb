# Proyecto de Gestión de Productos con GraphQL y Flask
Este proyecto implementa un sistema de gestión de productos utilizando Flask para el backend y GraphQL para la interfaz de consulta y mutación. Permite la inserción y consulta de productos a través de una API GraphQL.
## Uso
Asegúrate de tener Python y pip instalados en tu sistema.
Ejecuta el archivo app.py para iniciar el servidor Flask:
python app.py

## Estructura del Proyecto
El proyecto está estructurado de la siguiente manera:

- app.py: Archivo principal que configura la aplicación Flask y define las rutas.
- models.py: Archivo que contiene las definiciones de los tipos GraphQL, las consultas y las mutaciones.
- utils.py: Archivo con funciones auxiliares para cargar y guardar datos en un archivo JSON.
- productos.json: Archivo JSON que actúa como una base de datos de productos.

## Ejemplo de uso de queryGraphql
## insertar product
mutation {
  insertProduct(
    sku: "SKU999",
    name: "atril adulto",
    price: 24.09,
    brand: "artel ",
    description: "Atril de adulto :)")
  {
    product {
      sku
      name
      price
      brand
      description
    }
  }
}

## consultar productos
query {
  products {
    sku
    name
    price
    brand
    description
  }
}
