from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return 'Nos enorgullece presentarles una innovadora manera de disfrutar nuestra tradición más querida: el mate. En MATECH, hemos fusionado lo mejor de la tecnología con la esencia del mate tradicional, creando el primer mate convencional con control de temperatura. Con nuestro producto, podrán disfrutar de un mate siempre a la temperatura perfecta, sin preocuparse por conseguir agua caliente, que se enfríe o por quemarse. Matech está diseñado para mantener viva la pasión y el ritual del mate, adaptándose a las necesidades de la vida moderna. Gracias por acompañarnos en este viaje. ¡Salud y buenos mates!'
mates = [
    {'Modelo': 'small', 'stock': 8},
    {'Modelo': 'medium', 'stock': 14},
    {'Modelo': 'large', 'stock': 21},
]
@app.route('/mates', methods=['GET'])
def matesGet():
    return jsonify({'mates':mates, 'status':'ok' })

@app.route('/mates/<modelo>', methods=['GET'])
def matesGetx(modelo):
    for indice, p in enumerate(mates):
        print('p: ', p)
        print('mates:', mates)
        if p['Modelo'] == modelo:
            return jsonify({'mates':mates[indice], 'status':'ok' })
    return 'error'

@app.route('/mates', methods=['POST'])
def matesPost():
    body = request.json
    print(body)
    modelo = body['Modelo']
    stock = body['stock']

    newProd = {'Modelo': modelo, 'stock': stock}
    mates.append(newProd)

    return jsonify({'mates':mates, 'status':'ok' })

@app.route('/mates/<modelo>/operacion/<op>', methods=['PUT'])
def productopath(modelo, op):
    for indice, p in enumerate(mates):
        if p['Modelo'] == modelo:
            if op == 'venta':
                p['stock'] = p['stock'] -1
            if op == 'compra':
                p['stock'] = p['stock'] +1

    return jsonify({'mates':mates, 'status':'ok' })

@app.route('/mates', methods=['PUT'])
def matesbody():

    body = request.json
    modelo = body['Modelo']
    stock = body['stock']

    for indice, p in enumerate(mates):
        if p['Modelo'] == modelo:
            p['stock'] = stock
    return jsonify({'mates': mates, 'status': 'ok'})

@app.route('/mates/<modelo>', methods=['DELETE'])
def matesdelete(modelo):
    for indice, p in enumerate(mates):
        if p['Modelo'] == modelo:
            mates[indice: indice+1] = []
    return jsonify({'productos': mates, 'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)