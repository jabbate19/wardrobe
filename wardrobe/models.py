from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy.dialects.postgresql import UUID
import bcrypt

db = SQLAlchemy()

item_tag = db.Table('item_tag',
    db.Column('item_id', UUID(as_uuid=True), db.ForeignKey('wardrobe_items.id')),
    db.Column('tag', db.String(100), db.ForeignKey('tags.name'))
)

class WardrobeItem(db.Model):
    __tablename__ = 'wardrobe_items'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=db.func.current_timestamp())
    tags = db.relationship('Tag', secondary=item_tag, backref='wardrobe_items')

    def to_dict(self):
        return {
            'id': self.id.hex,
            'name': self.name,
            'date_added': self.date_added.isoformat(),
            'tags': [tag.name for tag in self.tags]
        }

class Tag(db.Model):
    __tablename__ = 'tags'
    
    name = db.Column(db.String(100), primary_key=True)

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