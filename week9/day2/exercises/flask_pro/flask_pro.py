from flask import Flask, request, render_template
from utils.functions import read_json
import json, os
import pandas as pd
from utils.data_mining_tb import df_info

# Mandatory
app = Flask(__name__)

# ----------- Flask functions -----------
'''
@app.route('/upload-dataset', methods=['GET', 'POST'])
def upload_dataset():
     if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            
            return df
'''
'''
@app.route('/')
def index():
    The Default path for the home screen
    return upload_dataset()
    #return app.send_static_file('upload-dataset.html')
'''




@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        return render_template('upload.html', shape=df.shape)
    return render_template('upload.html')



def main():
    print("---------STARTING PROCESS---------")
    print(os.path.dirname(os.getcwd()))
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    #settings_file = os.path.dirname(os.getcwd()) + os.sep + "settings.json"

    settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
    # Load json from file 
    json_readed = read_json(fullpath=settings_file)
    
    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]
    
    if SERVER_RUNNING:
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print("Server settings.json doesn't allow to start server. " + 
              "Please, allow it to run it.")

if __name__ == "__main__":
    main()