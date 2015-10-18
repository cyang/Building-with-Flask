import os
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from werkzeug import secure_filename

UPLOAD_FOLDER = '/Users/ChrisYang/Projects/Flask/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
index_bool=False

@app.route('/')
def index():
    return render_template('index_base.html', title="Index page", some_text = "This is the index page GUYS!", index_bool="True")

@app.route('/nicholas')
def nicholas_cage():
    return render_template('nicholas.html', title="Nicholas CAGE", some_text = "We are here for the A's", some_link="/", image = "https://cdn3.vox-cdn.com/thumbor/IE_0CtHTpjW1ix_Ztb5VHAdBHOE=/assets.sbnation.com/uploads/chorus_asset/file/2317732/nicolasCage_NotTheBees.0.gif")

@app.route('/panda')
def hello():
    return render_template('hello.html', title="Hello page", some_text= "Hello, I'm inheriting from index_base.html", some_link="/" , image="http://vignette2.wikia.nocookie.net/glee/images/7/7f/Panda_says_hi.gif/revision/latest?cb=20130503213951")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(debug=True)
