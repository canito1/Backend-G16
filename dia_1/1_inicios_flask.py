from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def inicio():
    if request.method == "PUT":
        return {"message":'Actualizacion exitosa'}, 202
    
    print(request.method)
    return {"message":'Hola mundo!'}
app.run()