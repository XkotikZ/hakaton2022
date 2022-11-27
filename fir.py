from flask import Flask, flash, render_template, redirect, request
from werkzeug.utils import secure_filename

import os
import pandas as pd
import numpy as np

from draw_on_gramota import gramota

app = Flask(__name__)

UPLOAD_FOLDER = r'C:/Users/Egor/Python/my_flask/f1/hakaton2022/hakaton2022'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['jpg', 'xlsx'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        example = request.files['example']
        info = request.files['info']
        save_file(example)
        save_file(info)

        processing_draw_on_diploma(example.name, info.name)

    return render_template('home.html')

def processing_draw_on_diploma(example_name, file_name):
    # filename = 'Spisko_nominatsiy_dlya_gramot.xlsx'
    # xls = pd.ExcelFile(filename)
    xls = pd.ExcelFile(file_name + '.xlsx')

    df = {}
    for name in xls.sheet_names:
        df[name] = pd.read_excel(xls, name)

    df_array = np.array(df[xls.sheet_names[0]])

    for d in df_array:
        date = str((d[3]).date()).replace('-', '.')
        gramota(example_name + '.jpg', f'{d[0]} {d[2]}.jpg', d[0], d[1], d[2], date,  d[4], show=False, save=True)

@app.route('/hello')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run()