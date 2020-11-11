from flask import Flask, request, render_template
import random
import operator

# Configuraciones
app = Flask(__name__)

# Rutas del api
@app.route('/random', methods=['GET'])
def m_random():
    turno = request.args.get('turno')
    turno = int(turno)
    estado = request.args.get('estado')
    matriz = [[0 for x in range(8)] for x in range(8)]
    mov = []
    c = 0
    #transformacion lineal a matriz
    for x in range(8):
        for y in range(8):
            a = estado[c]
            matriz[x][y] = int(a)
            c = c + 1

    #busqueda de movimientos
    for x in range(8):
        for y in range(8):
            if matriz[x][y]==turno:
                #norte
                if x >1:
                    norte(matriz, mov, turno, x, y)
                #sur
                if x<6:
                    sur(matriz, mov, turno, x, y)
                #oeste
                if y>1:
                    oeste(matriz, mov, turno, x, y)
                #este
                if y<6:
                    este(matriz, mov, turno, x, y)
                #noroeste
                if x>1 and y>1:
                    noroeste(matriz, mov, turno, x, y)
                #noreste
                if x>1 and y<6:
                    noreste(matriz, mov, turno, x, y)
                #suroeste
                if x<6 and y>1:
                    suroeste(matriz, mov, turno, x, y)
                #sureste
                if x<6 and y<6:
                    sureste(matriz, mov, turno, x, y)
    max = len(mov)-1
    indice = random.randint(0, max)
    return render_template("index.html",
                           mycontent=str(mov[indice]))


@app.route('/heuristica', methods=['GET'])
def m_heuristica():
    turno = request.args.get('turno')
    turno = int(turno)
    estado = request.args.get('estado')
    matriz = [[0 for x in range(8)] for x in range(8)]
    mov = []
    c = 0
    #transformacion lineal a matriz
    for x in range(8):
        for y in range(8):
            a = estado[c]
            matriz[x][y] = int(a)
            c = c + 1

    #busqueda de movimientos
    for x in range(8):
        for y in range(8):
            if matriz[x][y]==turno:
                #norte
                if x >1:
                    norte(matriz, mov, turno, x, y)
                #sur
                if x<6:
                    sur(matriz, mov, turno, x, y)
                #oeste
                if y>1:
                    oeste(matriz, mov, turno, x, y)
                #este
                if y<6:
                    este(matriz, mov, turno, x, y)
                #noroeste
                if x>1 and y>1:
                    noroeste(matriz, mov, turno, x, y)
                #noreste
                if x>1 and y<6:
                    noreste(matriz, mov, turno, x, y)
                #suroeste
                if x<6 and y>1:
                    suroeste(matriz, mov, turno, x, y)
                #sureste
                if x<6 and y<6:
                    sureste(matriz, mov, turno, x, y)

    max = len(mov)-1
    indice = BusquedaPorAdversario(max, mov)

    return render_template("index.html",
                           mycontent=str(mov[indice]))

def getTurno(turno):
    return 1 if turno == 0 else 0

def norte(matriz, mov, turno, x, y):
    if matriz[x - 1][y] == getTurno(turno):
        # print("norte")
        a = x - 2
        while a >= 0:
            if matriz[a][y] == 2:
                mov.append(str(a) + str(y))
                break
            elif matriz[a][y] == turno:
                break
            a = a - 1

def sur(matriz, mov, turno, x, y):
    if matriz[x + 1][y] == getTurno(turno):
        # print("sur")
        a = x + 2
        while a <= 7:
            if matriz[a][y] == 2:
                mov.append(str(a) + str(y))
                break
            elif matriz[a][y] == turno:
                break
            a = a + 1

def oeste(matriz, mov, turno, x, y):
    if matriz[x][y - 1] == getTurno(turno):
        # print("oeste")
        a = y - 2
        while a >= 0:
            if matriz[x][a] == 2:
                mov.append(str(x) + str(a))
                break
            elif matriz[x][a] == turno:
                break
            a = a - 1

def este(matriz, mov, turno, x, y):
    if matriz[x][y + 1] == getTurno(turno):
        # print("este")
        a = y + 2
        while a <= 7:
            if matriz[x][a] == 2:
                mov.append(str(x) + str(a))
                break
            elif matriz[x][a] == turno:
                break
            a = a + 1

def noroeste(matriz, mov, turno, x, y):
    if matriz[x - 1][y - 1] == getTurno(turno):
        # print("noroeste")
        a = x - 2
        b = y - 2
        while a >= 0 and b >= 0:
            if matriz[a][b] == 2:
                mov.append(str(a) + str(b))
                break
            elif matriz[a][b] == turno:
                break
            a = a - 1
            b = b - 1

def noreste(matriz, mov, turno, x, y):
    if matriz[x - 1][y + 1] == getTurno(turno):
        # print("noreste")
        a = x - 2
        b = y + 2
        while a >= 0 and b <= 7:
            if matriz[a][b] == 2:
                mov.append(str(a) + str(b))
                break
            elif matriz[a][b] == turno:
                break
            a = a - 1
            b = b + 1

def suroeste(matriz, mov, turno, x, y):
    if matriz[x + 1][y - 1] == getTurno(turno):
        # print("suroeste")
        a = x + 2
        b = y - 2
        while a <= 7 and b >= 0:
            if matriz[a][b] == 2:
                mov.append(str(a) + str(b))
                break
            elif matriz[a][b] == turno:
                break
            a = a + 1
            b = b - 1

def sureste(matriz, mov, turno, x, y):
    if matriz[x + 1][y + 1] == getTurno(turno):
        # print("sureste")
        a = x + 2
        b = y + 2
        while a <= 7 and b <= 7:
            if matriz[a][b] == 2:
                mov.append(str(a) + str(b))
                break
            elif matriz[a][b] == turno:
                break
            a = a + 1
            b = b + 1

def BusquedaPorAdversario(max, mov):
    heuristica = [
        [120, -20, 20,  5,  5, 20, -20, 120],
        [-20, -40, -5, -5, -5, -5, -40, -20],
        [ 20,  -5, 15,  3,  3, 15,  -5,  20],
        [  5,  -5,  3,  3,  3,  3,  -5,   5],
        [  5,  -5,  3,  3,  3,  3,  -5,   5],
        [ 20,  -5, 15,  3,  3, 15,  -5,  20],
        [-20, -40, -5, -5, -5, -5, -40, -20],
        [120, -20, 20,  5,  5, 20, -20, 120]
    ]

    valor = {}
    a=0
    while a<=max:
        x=int(mov[a][0])
        y=int(mov[a][1])
        valor[a]=heuristica[x][y]
        a=a+1

    # ordenar por maximo valor
    list_sort = sorted(valor.items(), key=operator.itemgetter(1), reverse=True)
    tuple_result = list_sort[0]
    indice = tuple_result[0]
    return indice
