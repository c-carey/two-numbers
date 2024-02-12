from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')


def index():
    return render_template("index.html")


@app.route('/result')


def result():
    first = int(request.args.get('first'))
    second = int(request.args.get('second'))
    operand = str(request.args.get('operand'))
    if operand == "+":
        result = first + second
    if operand == "-":
        result = first - second
    if operand == "*":
        result = first * second
    if operand == "/" and second != 0:
        result = first / second
    if operand == "/" and second == 0:
        result = "Division by zero not supported"
    return render_template("result.html", result=result, first=first, second=second, operand=operand)


if __name__ == "__main__":
    app.run()
