from flask import Flask, request, flash, url_for
from flask_cors import CORS
from markupsafe import escape
import random

# Configuraciones
app = Flask(__name__)
CORS(app)

def op(turno):
    if turno ==0:
        return 1
    else:
        return 0

# Rutas del api
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, cross-origin-world!"

@app.route('/grupo/<int:group_id>', methods=['GET'])
def getgrupo(group_id):
    return 'form_grupo ' + str(group_id)

@app.route('/data', methods=['GET'])
def data():
    # here we want to get the value of user (i.e. ?user=some-value)
    user = request.args.get('user')
    return user

@app.route('/random', methods=['GET'])
def m_random():
    turno = request.args.get('turno')
    estado = request.args.get('estado')
    matriz = [[0 for x in range(8)] for x in range(8)]
    mov = []
    c = 0
    #transformacion lineal a matriz
    for x in range(8):
        for y in range(8):
            matriz[x][y] = estado[c]
            c = c + 1

    #busqueda de movimientos
    for x in range(8):
        for y in range(8):
            if matriz[x][y]==turno:
                #norte
                if x >1:
                    if matriz[x-1][y] == op(turno):
                        a=x-2
                        while a>=0:
                            if matriz[a][y]==2:
                                mov.append(str(a)+str(y))
                                break
                            elif matriz[a][y]==turno:
                                break
                            a=a-1
		#sur
                if x<6:
                    if matriz[x+1][y]==op(turno):
                        a=x+2
                        while a<=7:
                            if matriz[a][y]==2:
                                mov.append(str(a)+str(y))
                                break
                            elif matri[a][y]==turno:
                                break
                            a=a+1
                #oeste
                if y>1:
                    if matriz[x][y-1]==op(turno):
                        a=y-2
                        while a>=0:
                            if matriz[x][a]==2:
                                mov.append(str(x)+str(a))
                                break
                            elif matriz[x][a]==turno:
                                break
                            a=a-1
                #este
                if y<6:
                    if matriz[x][y+1]==op(turno):
                        a=y+2
                        while a<=7:
                            if matriz[x][a]==2:
                                mov.append(str(x)+str(a))
                                break
                            elif matriz[x][a]==turno:
                                break
                            a=a+1
                #noroeste
                if x>1 and y>1:
                    if matriz[x-1][y-1]==op(turno):
                        a = x - 2
                        b = y - 2
                        while a >= 0 and b >= 0:
                            if matriz[a][b]==2:
                                mov.append(str(a)+str(b))
                                break
                            elif matriz[a][b]==turno:
                                break
                            a=a-1
                            b=b-1
                #noreste
                if x>1 and y<6:
                    if matriz[x-1][y+1]==op(turno):
                        a=x-2
                        b=y+2
                        while a>=0 and b<=7:
                            if matriz[a][b]==2:
                                mov.append(str(a)+str(b))
                                break
                            elif matriz[a][b]==turno:
                                break
                            a=a-1
                            b=b-1
                #suroeste
                if x<6 and y>1:
                    if matriz[x+1][y-1]==op(turno):
                        a=x+2
                        b=y-2
                        while a<=7 and b>=0:
                            if matriz[a][b]==2:
                                mov.append(str(a)+str(b))
                                break
                            elif matriz[a][b]==turno:
                                break
                            a=a+1
                            b=b-1
                #sureste
                if x<6 and y<6:
                    if matriz[x+1][y+1]==op(turno):
                        a=x+2
                        b=y+2
                        while a<=7 and b<=7:
                            if matriz[a][b]==2:
                                mov.append(str(a)+str(b))
                                break
                            elif matriz[a][b]==turno:
                                break
                            a=a+1
                            b=b+1
    print(turno)
    print(estado)
    print(matriz)
    max = len(mov)
#    indice = random.randint(0, max)
 #   print(mov[indice])
    return str(max)
