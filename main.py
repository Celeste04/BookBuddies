from flask import Flask, render_template, request, jsonify, session
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
import ai
from wtforms.validators import InputRequired
import ai
import skills

# vars
UPLOAD_DIR = './uploads'
file_path = ''
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = ''

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    current_skills = ''
    if form.validate_on_submit():
        uploaded_file = form.file.data # First grab the file
        #file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        file_path = os.path.join(UPLOAD_DIR, secure_filename(uploaded_file.filename))

        # Ensure the 'uploads' directory exists, create it if necessary
        if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)
        # Save file to uploads directory
        uploaded_file.save(file_path)
        session['file_path'] = file_path
        current_skills = skills.extract_skills_from_resume(file_path)
    return render_template('index.html', form=form, current_skills=current_skills)

@app.route('/process-form', methods=['POST'])
def process_form():
    form=UploadFileForm()
    job_skills=''
    file_path = session.get('file_path')
    print("hi:", file_path)
    if request.method == 'POST':
        job_desc = request.form['jobRequirements']
        job_skills = skills.extract_skills(job_desc)
        missing_skills = skills.missing_skills(file_path, job_desc)
        matched_skills = skills.matched_skills(len(job_skills)) - len(missing_skills), len(job_skills))
    return render_template('index.html', form=form, job_skills=job_skills, missing_skills=missing_skills)

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return ai.get_Chat_response(input)

def get_Chat_response(text):
    ai.getQuestions()

if __name__ == '__main__':
    app.run(debug=True)

