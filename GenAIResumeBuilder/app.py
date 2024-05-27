from flask import Flask, render_template, request, send_file, redirect, jsonify
from werkzeug.utils import secure_filename
import os, glob
import zipfile
from src.constants import Config
from src.TextExtractor import TextExtractor
from src.OpenAIClient import OpenAIClient
from src.ResumeGenerator import ShortResumeGenerator, LongResumeGenerator

app = Flask(__name__)
upload_folder = Config.UPLOAD_FOLDER
output_folder = Config.OUTPUT_FOLDER

processing_result = {"converted_resumes": [], "failed_resumes": []}
uploaded_files = []
progress = 0

if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


def cleanup():
    global uploaded_files
    processing_result["converted_resumes"] = []
    processing_result["failed_resumes"] = []
    uploaded_files = []
    for file in glob.glob(output_folder + "/*"):
        os.remove(file)
    for file in glob.glob(upload_folder + "/*"):
        os.remove(file)
    if os.path.isfile("output.zip"):
        os.remove("output.zip")


@app.route("/")
def index():
    cleanup()
    return render_template("index.html", result=None, download_link=None)


@app.route("/uploaded", methods=["POST"])
def upload_file():
    if "resume" not in request.files:
        return render_template("index.html", result="No file found")

    files = request.files.getlist("resume")

    for file in files:
        file_name = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, file_name)
        file.save(file_path)
        uploaded_files.append(file_name)
    return render_template("uploaded_files.html", uploaded_files=uploaded_files)


@app.route("/convert", methods=["POST"])
def convert():
    summary_type = request.form.get("summaryType", "original")

    for file_name in uploaded_files:
        try:

            text = TextExtractor(os.path.join(upload_folder, file_name)).extract_text()
            json_object = OpenAIClient(text, summary_type).process_text()

            if summary_type == "short":
                ShortResumeGenerator(json_object, summary_type).generate()
            else:
                LongResumeGenerator(json_object, summary_type).generate()

            processing_result["converted_resumes"].append(file_name)
        except Exception as e:
            print(f"Error processing {file_name} : {e}")
            processing_result["failed_resumes"].append(file_name)

    return redirect('/converted')


@app.route("/download")
def download_file():
    output_files = os.listdir(output_folder)
    if len(output_files) == 1:
        # If there's only one file, send it directly without zipping
        return send_file(os.path.join(output_folder, output_files[0]), as_attachment=True)
    else:
        # If there are multiple files, create a zip archive
        with zipfile.ZipFile("output.zip", "w") as zf:
            for dirname, subdirs, files in os.walk(output_folder):
                for file in files:
                    zf.write(os.path.join(dirname, file))
        return send_file("output.zip", as_attachment=True)


@app.route("/converted")
def render_converted():
    return render_template("converted.html", processing_result=processing_result)


@app.route("/progress")
def track_progress():
    global progress
    total_num_files = len(uploaded_files)
    processed_num_files = len(processing_result['converted_resumes']) + len(processing_result['failed_resumes'])
    progress = (processed_num_files / total_num_files) * 100
    return jsonify({"progress": progress})


@app.route("/start")
def start_task():
    global progress
    progress = 0
    return "Started"


@app.route('/delete/<path:file_name>', methods=["GET"])
def delete(file_name):
    uploaded_files.remove(file_name)
    return render_template('uploaded_files.html', uploaded_files=uploaded_files)


@app.route('/add')
def add():
    return render_template('index.html')

@app.after_request
def add_no_cache(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
