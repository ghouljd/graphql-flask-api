from flask import Flask, request
from flask_cors import CORS
from flask_graphql import GraphQLView
from schema import schema
from models import session

app = Flask(__name__)
CORS(app)

def custom_context():
    return {
        'request': request,
        'session': session
    }

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,
        get_context=custom_context
    )
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
