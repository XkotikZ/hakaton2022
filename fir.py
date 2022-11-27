from flask import Flask, flash, render_template, redirect, request

app = Flask(__name__)

menu = ['установка', 'первое приложени', 'клик']
a = 1

@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        print('file' not in request.files)
        if 'file' not in request.files:
            flash('Нет файла')
    #         return redirect(request.url)
    #     file = request.files['file']
    #     # print(file)

    global a
    a += a
    return render_template('home.html', title='Main', body='page body', a=round(a, 2), menu=menu)

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/hell')
def help():
    return 'Help!'

@app.route('/set/<int:i>')
def set_name(i):
    global a
    a = i
    return render_template('home.html', title='Main', body='page body', a=round(a, 2), menu=menu)
    # return f"<p>число: {i}</p>"

if __name__ == '__main__':
    app.debug = True
    app.run()