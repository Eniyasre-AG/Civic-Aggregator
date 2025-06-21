import os
from werkzeug.utils import secure_filename

def save_uploaded_image(file, upload_folder):
    filename = secure_filename(file.filename)
    filepath = os.path.join(upload_folder, filename)
    file.save(filepath)
    return filepath
