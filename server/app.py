#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def url_says(parameter):
    browse = f'{parameter}'
    print(parameter)
    return browse

@app.route('/count/<int:parameter>')
def count(parameter):
    string = ''
    for x in range(parameter):
        string += f'{x}\n'
           
    return f'{string}'

@app.route('/math/<int:num1>/<op>/<int:num2>')
def something(num1,op,num2):
    if op == '+':
        return f'{num1+num2}'
    elif  op == '-':
        return f'{num1-num2}'
    elif  op == 'div':
        return f'{num1/num2}'
    elif op == '*':
        return f'{num1*num2}'
    elif op == '%':
        return f'{num1%num2}'
    else:
        return 'input an operator goofy lookin ass'

    return f'{num1,op, num2}'
# def adding(num1, num2):
#     print(f'num1 is a {type(num1)}')
#     print(f'num2 is a {type(num2)}')
#     return f'<h1>{num1+num2}</h1>'
    



if __name__ == '__main__':
    app.run(port=5555, debug=True)


