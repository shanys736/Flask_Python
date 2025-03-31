from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    n = 5
    for i in range(1, n + 1):
        for j in range(n -i ):
            print(" ", end="")
            for k in range(i):
                print("*", end="")
                print()
            etoiles +='<br>'
    return etoiles


if __name__ == "__main__":
  app.run(debug=True)
