# models.py
import graphene
from utils import load_products_from_json, save_product_in_json

class UserType(graphene.Enum):
    ADMIN = "ADMIN"
    ANONYMOUS = "ANONYMOUS"

class Product(graphene.ObjectType):
    sku = graphene.String()
    name = graphene.String()
    price = graphene.Float()
    brand = graphene.String()
    description = graphene.String()

# Definición de mutaciones GraphQL para insertar un nuevo producto
class InsertProduct(graphene.Mutation):
    class Arguments:
        sku = graphene.String(required=True)
        name = graphene.String(required=True)
        price = graphene.Float(required=True)
        brand = graphene.String(required=True)
        description = graphene.String()

    product = graphene.Field(Product)

    def mutate(self, info, sku, name, price, brand, description=None):
        new_product = {
            'sku': sku,
            'name': name,
            'price': price,
            'brand': brand,
            'description': description
        }
        
        save_product_in_json(new_product)     
        return InsertProduct(product=new_product)

# Definición de consultas GraphQL
class Query(graphene.ObjectType):
    #producto = graphene.Field(Product)
    products = graphene.List(Product)
    def resolve_products(self, info):
        # Cargar los productos desde el archivo JSON
        products_json = load_products_from_json()
        # Convertir los productos JSON en objetos Producto GraphQL
        products = [Product(
            sku=product['sku'],
            name=product['name'],
            price=product['price'],
            brand=product['brand'],
            description=product['description']
        ) for product in products_json]
        
        return products

class Mutations(graphene.ObjectType):
    insert_product = InsertProduct.Field()

