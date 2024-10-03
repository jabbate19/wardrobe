from . import api_bp
from flask import request, jsonify
from ..models import db, WardrobeItem
from ..app import s3, app
from botocore.exceptions import NoCredentialsError
from flask_login import login_required

def upload_to_s3(file, bucket_name, uuid):
    try:
        s3.upload_fileobj(
            file,
            bucket_name,
            uuid,
            ExtraArgs={'ACL': 'public-read'}
        )
    except NoCredentialsError:
        return None

@api_bp.route('/items', methods=['POST'])
#@login_required
def add_item():
    name = request.form['name']
    file = request.files['image']
    new_item = WardrobeItem(name=name)
    db.session.add(new_item)
    db.session.commit()
    db.session.refresh(new_item)

    if file:
        upload_to_s3(file, app.config['S3_BUCKET'], new_item.id.hex)
    else:
        return jsonify({'error': 'Image upload failed'}), 400

    return jsonify(new_item.to_dict()), 201


@api_bp.route('/items', methods=['GET'])
@login_required
def get_items():
    items = WardrobeItem.query.all()
    return jsonify([item.to_dict() for item in items])