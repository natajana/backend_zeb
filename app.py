# app.py
from flask import Flask
from flask_graphql import GraphQLView
import graphene
from models import UserType, Query, Mutations

# Mock user database
user_db = {
    "admin1": {"username": "admin1", "type": UserType.ADMIN},
    "admin2": {"username": "admin2", "type": UserType.ADMIN},
    "anonymous1": {"username": "anonymous1", "type": UserType.ANONYMOUS},
    # Add more users as needed
}

# Configuración de la aplicación Flask
app = Flask(__name__)

# Configuración del esquema GraphQL
schema = graphene.Schema(query=Query, mutation=Mutations)

# Ruta para la vista GraphQL
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(debug=True)
