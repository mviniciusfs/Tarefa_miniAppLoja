import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def lista():  # put application's code here
    #TODO
    #Criar m dicionário para produtos com nome, preço e img
    lista_prod = {'#1':
                      ['Arroz Sepé', 'R$20,99', 'https://www.extrabom.com.br/uploads/produtos/350x350/7859_7896009865657.jpg'],
                  '#2':
                      ['Feijão Ana', 'R$7,99', 'https://wilso.agilecdn.com.br/4206_1.jpg'],
                  '#3':
                      ['Fubá Yoki', 'R$5,99', 'https://api.tendaatacado.com.br/fotos/4853_big.jpg']
                  }
    return render_template('index.html')

if __name__ == '__main__':
    app.run()