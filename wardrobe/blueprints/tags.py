from . import api_bp
from flask import jsonify
from ..models import Tag
from flask_login import login_required

@api_bp.route('/tags', methods=['GET'])
@login_required
def get_tags():
    tags = Tag.query.all()
    return jsonify([tag.name for tag in tags])
