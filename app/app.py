from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from models import db, Issue
from ml import classify_text, cluster_issues
from utils import save_uploaded_image
from emailer import send_email_report
from auth import login_route
from flask import flash 
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a secure key from env in production

# ------------------ Config ------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///issues.db'
app.config['UPLOAD_FOLDER'] = 'app/uploads'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ------------------ Init DB & Auth ------------------
db.init_app(app)
login_route(app)

# Create DB tables if not exists
with app.app_context():
    db.create_all()

# ------------------ Auto Login (For Testing Only) ------------------
@app.before_request
def auto_login():
    session['admin'] = True  # REMOVE or disable this for production

# ------------------ Routes ------------------

# 📍 Report Form (Submit Page)
@app.route('/')
def index():
    return render_template('index.html')

# 📝 Handle Report Submission

@app.route('/report', methods=['POST'])
def report_issue():
    file = request.files['image']
    desc = request.form['description']
    lat = float(request.form.get('lat', 0))
    lon = float(request.form.get('lon', 0))

    filepath = save_uploaded_image(file, app.config['UPLOAD_FOLDER'])
    tag = classify_text(desc)

    issue = Issue(description=desc, tag=tag, image_path=filepath, latitude=lat, longitude=lon)
    db.session.add(issue)
    db.session.commit()

    # Send email
    send_email_report(desc, tag, filepath, lat, lon)

    # 🎉 Show message to user (on the same page)
    flash("✅ Report successfully submitted and sent to the authority!")
    return redirect('/')

# 🔐 Admin Dashboard (Map View)
@app.route('/dashboard')
def dashboard():
    if not session.get('admin'):
        return redirect('/login')

    issues = Issue.query.all()

    def to_dict(issue):
        return {
            'id': issue.id,
            'description': issue.description,
            'tag': issue.tag,
            'image_path': issue.image_path,
            'latitude': issue.latitude,
            'longitude': issue.longitude
        }

    issue_dicts = [to_dict(issue) for issue in issues]

    return render_template('dashboard.html', issues=issue_dicts)

# 🖼 Serve uploaded images
@app.route('/app/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# ------------------ Main ------------------
if __name__ == '__main__':
    print("Starting Flask app...")
    app.run(debug=True)
