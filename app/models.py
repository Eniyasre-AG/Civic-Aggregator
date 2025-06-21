from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    tag = db.Column(db.String(50), nullable=False)
    image_path = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    cluster_id = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
