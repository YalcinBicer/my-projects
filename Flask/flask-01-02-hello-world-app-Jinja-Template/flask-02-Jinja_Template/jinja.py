from flask import Flask, render_template  # Falsk ve render_template kütüphaneliri yüklenir

app = Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html", number1=12345789, number2=987654321) # index.html kiralanır

@app.route("/sum")
def number():
    num1 = 55
    num2 = 10
    return render_template("body.html", value1 = num1, value2 = num2, sum = num1 + num2) # body.html kiralanır

if __name__== "__main__":
    app.run(debug=True)