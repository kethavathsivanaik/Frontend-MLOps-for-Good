from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__)
@app.route('/')
def home():
        return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
     if request.method == 'POST':  
        file = request.files['file']
        file.save(file.filename)
        return  redirect("/")
        
        

if __name__ == '_main_':
        app.run(host='0.0.0.0')
