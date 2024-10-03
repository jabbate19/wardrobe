from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy.dialects.postgresql import UUID
import bcrypt

db = SQLAlchemy()

class WardrobeItem(db.Model):
    __tablename__ = 'wardrobe_items'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id.hex,
            'name': self.name,
            'date_added': self.date_added.isoformat(),
        }

class User(db.Model):
    __tablename__ = 'users'
    
    username = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(255), nullable=False)

    def authenticate(self, password):
        return bcrypt.checkpw(password.encode(), self.password.encode())

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    def get_id(self):
        return self.username