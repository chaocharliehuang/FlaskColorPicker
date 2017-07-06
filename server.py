from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pickcolor', methods=['POST'])
def change_bg_color():
    red = int(request.form['red'])
    green = int(request.form['green'])
    blue = int(request.form['blue'])
    return render_template('index.html', red=red, green=green, blue=blue)

app.run(debug=True)