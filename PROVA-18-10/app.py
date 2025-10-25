from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/soma')
def soma():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))
    
    soma = n1 + n2 
    
    return{

        'numero1': n1,
        'numero2': n2,
        'soma dos 2 numeros': soma

          }

@app.route('/subtração')
def subtração():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))
    
    subtração = n1 + n2 
    
    return{

        'numero1': n1,
        'numero2': n2,
        'subitração dos 2 numeros': subtração

          }

@app.route('/divisão')
def divisão():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))
    
    divisão = n1 + n2 
    
    return{

        'numero1': n1,
        'numero2': n2,
        'divisão dos 2 numeros': divisão

          }

@app.route('/adição')
def adição():
    n1 = int(request.args.get('valor1',0))
    n2 = int(request.args.get('valor2',0))
    
    adição = n1 + n2 
    
    return{

        'numero1': n1,
        'numero2': n2,
        'adiçaõ dos 2 numeros': adição

          }
   
if __name__ == "__main__":
    app.run(debug=True, port=5002)