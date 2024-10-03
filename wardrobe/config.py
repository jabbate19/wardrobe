import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # S3 Config
    S3_BUCKET = os.getenv('S3_BUCKET_NAME')
    S3_KEY = os.getenv('S3_ACCESS_KEY_ID')
    S3_SECRET = os.getenv('S3_SECRET_ACCESS_KEY')
    S3_ENDPOINT = os.getenv('S3_ENDPOINT')
    SECRET_KEY = os.getenv('SECRET_KEY')
