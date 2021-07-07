import os
from flask import Flask, render_template, request, redirect, url_for
#from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename


app=Flask(__name__)



UPLOAD_FOLDER = r"/app/UI/static/ml/"

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
            ext=file.filename.rsplit('.', 1)[1].lower()       
            cmd="python"+" "+r"/app/script.py"+" "+UPLOAD_FOLDER+file.filename
            
            os.system(cmd)
            if os.path.isfile(r"/app/UI/static/ml/pred.jpg"):
                pred="pred.jpg"

                return redirect(url_for("final",name="Brain Tumor Predicted",pred=pred))
            else:
                pred=file.filename
                return  redirect(url_for("final",name="You are free from Brain Tumor",pred=pred))
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
    name=request.args['name']
    pred=request.args['pred']
    return render_template('final.html',variable=name,filepath=pred)








app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

if __name__ == '_main_':
        app.run(host='0.0.0.0')
