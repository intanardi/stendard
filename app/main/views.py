from datetime import datetime
from flask import render_template, session, redirect, request, jsonify, Flask, url_for, flash
from . import main
from .. import db, csrf
from ..models import *
from werkzeug.utils import secure_filename
from ..utils import generate_token, verify_token
import random
import os
from os.path import join, dirname, realpath
import re
from webdav3.client import Client
from requests_ntlm import HttpNtlmAuth


options = {
 'webdav_hostname':  "http://localhost:5000"
}

client = Client(options)
client.session.auth = HttpNtlmAuth('http://localhost:5000\\username','password')


UPLOAD_FOLDER = 'static/uploads/'
apps = Flask(__name__)
apps.config['UPLOAD_PATH'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'docx', 'xlsx', 'pptx', 'xls'}


def allowed_file(filename):
    return '.' in filename and \
    filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/', methods=['GET', 'POST'])
@csrf.exempt
def index():
    if request.method == 'POST':
        myfile = request.files['myfile']
        check_file = allowed_file(myfile.filename)
        if check_file is not True:
            flash('File is not allowed')
            return redirect(request.url)
        if myfile.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # get_extension = myfile.filename.split(".")
        # myfilename = str(random.randint(1, 100000))
        # myfilename = myfilename+ '.'+ str(get_extension[-1])
        myfile.save(os.path.join(apps.config['UPLOAD_PATH'],myfile.filename))
        document = Document()
        document.filename = myfile.filename
        document.created_date = datetime.now()
        db.session.add(document)
        db.session.commit()
        
        return redirect(url_for('main.data'))
    return render_template('index.html')

@main.route('/data', methods=['GET', 'POST'])
def data():
    data = Document.query.all()
    return render_template('data.html', data=data)

@main.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    document = Document.query.filter_by(id=id).first()
    print(document.filename)
    # client.info(UPLOAD_FOLDER+document.filename)
    os.system(UPLOAD_FOLDER+document.filename)
    # client.download_sync(remote_path=UPLOAD_FOLDER+'/'+document.filename, local_path="~/Downloads/"+document.filename)
    return redirect(url_for('main.data'))