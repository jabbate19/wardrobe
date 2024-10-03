from flask import Flask, send_from_directory
from .models import db, User
from .config import Config
import boto3
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

# S3 Client Setup
s3 = boto3.client(
    "s3",
    endpoint_url=app.config['S3_ENDPOINT'],
    aws_access_key_id=app.config['S3_KEY'],
    aws_secret_access_key=app.config['S3_SECRET']
)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from .blueprints import api_bp  # noqa: E402

app.register_blueprint(api_bp, url_prefix="/api")

@app.route('/favicon.ico')
def send_favicon():
    return send_from_directory('dist', 'favicon.ico')

@app.route('/assets/<path:path>')
def send_file(path):
    return send_from_directory('dist/assets', path)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def send_index(path):
    return send_from_directory('dist', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
