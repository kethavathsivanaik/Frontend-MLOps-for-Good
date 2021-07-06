import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
app=Flask(__name__)



UPLOAD_FOLDER = r"C:\Users\SRIDHAR RAO\Desktop\files"

@app.route('/')
def home():
        return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
     if request.method == 'POST':  
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            app.config["MONGO_URI"] = "mongodb://localhost:27017/mlops"
            mongodb_client = PyMongo(app)
            db = mongodb_client.db
            db.mlops1.insert({"name":"test","image":UPLOAD_FOLDER})
            #return  redirect("/")
            #var =db.mlops.aggregate()
            return  redirect("/final")
            # else:
            #     return "No Duplicate"
        else:
            return  redirect("/wrong")
        


ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/wrong')
def wrong():
    return render_template('wrong.html')
@app.route('/final')
def final():
    return render_template('final.html')








app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

if __name__ == '_main_':
        app.run(host='0.0.0.0')
