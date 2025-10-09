from urllib import request
from flask import Flask, render_template, request
import random
a = []
app = Flask(__name__)

wsgi_app = app.wsgi_app

@app.route('/')
def func1():
    return render_template("index.html")

@app.route('/',methods=['POST'])
def func2():
    value1 = request.form.get('textbox1')
    value2 = request.form.get('textbox2')
    ivalue1 = int(value1)
    ivalue2 = int(value2)
    i = ivalue2
    while i >= 1:
        a.append(i)
        i = i - 1
    ivalue3 = int(random.randint(1, random.choice(a)))

    for c in a[::-1]:
        if c == ivalue3:
            a.remove(c)

    result = "結果:" + str(ivalue3)
    return render_template("index.html", output_message=result)
    
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
