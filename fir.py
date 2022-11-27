from flask import Flask, flash, render_template, redirect, request

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
    # if request.method == 'POST':
        # print('file' not in request.files)
        # if 'file' not in request.files:
            # flash('Нет файла')
    #         return redirect(request.url)
    #     file = request.files['file']
    #     # print(file)

    return render_template('home.html')

@app.route('/hello')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run()