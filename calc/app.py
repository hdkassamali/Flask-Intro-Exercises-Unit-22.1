from flask import Flask, request
from operations import add, sub, div, mult

app = Flask(__name__)


@app.route("/add")
def add_nums():
    """Add a and b parameters"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))


@app.route("/sub")
def sub_nums():
    """Subtract a and b parameters"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)
    return str(result)


@app.route("/mult")
def mult_nums():
    """Multiply a and b parameters"""

    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))


@app.route("/div")
def div_nums():
    """Divide a and b parameters"""
    
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))


operators = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,

}
@app.route("/math/<oper>")
def perfom_math(oper):
    """Do math on a and b."""
    a = int(request.args["a"])
    b = int(request.args["b"])

    # if operation == "add":
    #     return str(add(a, b))
    # elif operation == "sub":
    #     return str(sub(a, b))
    # elif operation == "mult":
    #     return str(mult(a, b))
    # elif operation == "div":
    #     return str(div(a, b))
    return str(operators[oper](a, b))
