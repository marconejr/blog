from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

#lista com dicionário 
# mock -> substituto um preenchimento default para simulação
posts = [
    {
        "title":"o Meu primeiro Post", 
        "body": "Aqui é o texto do Post",
        "author": "Marcone",
        "created": datetime(2022,7,25)
    },

    {
        "title":"o Meu segundo Post", 
        "body": "Aqui é o texto do Post",
        "author": "Marcone",
        "created": datetime(2022,7,26)
    },
]

@app.route("/")

def index():
    return render_template("index.html", posts=posts)


@app.route('/login')
def login():
    return render_template("login.html")
