from flask import Flask

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>Hello World!!!</h1>"

@app.route("/second")
def second():
    return "<h1>Hello World From Flask!!!</h1>"

@app.route("/third/subthird")
def third():
    return "<h2>This is the subpath of third page</h2>"

@app.route("/forth/<string:id>")
def forth(id):
    return f"<h2>Id of this page is {id}"


if __name__ == '__main__':
    app.run(debug=True)             # localhost:5000 portundan yayın yapar.
    # app.run(debug=True, port=4000)  # Farklı bir porttan yayınlamak istediğimizde
