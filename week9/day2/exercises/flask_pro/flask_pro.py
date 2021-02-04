from flask import Flask, request, render_template
from utils.functions import read_json
import json, os

# Mandatory
app = Flask(__name__)

# ----------- Flask functions -----------
@app.route('/')
def index():
    ''' The Default path for the home screen '''
    render_template('upload.html')

@app.route('/upload-dataset', methods=['GET', 'POST'])
def upload_image():
    return render_template('static/upload_dataset.html')