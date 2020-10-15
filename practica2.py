from flask import Flask, request, flash, url_for
from flask_cors import CORS
from markupsafe import escape

# Configuraciones
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, cross-origin-world!"


# Rutas del api
@app.route('/grupo/<int:group_id>', methods=['GET'])
def getgrupo(group_id):
    return 'form_grupo ' + str(group_id)

@app.route('/data', methods=['GET'])
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')
    return user
