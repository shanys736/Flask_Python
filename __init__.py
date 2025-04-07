from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    nombre = ''
    for j in range(valeur):
        for i in range(valeur-j):
            nombre += '+'
            for k in range(j+1):
                nombres += '*'
                nombres += '<br>'
    return nombres


if __name__ == "__main__":
  app.run(debug=True)
