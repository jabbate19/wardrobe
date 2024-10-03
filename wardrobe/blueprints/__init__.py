from flask import Blueprint
api_bp = Blueprint('api', __name__)
from . import items, auth, tags  # noqa: E402
__all__ = ['items', 'auth', 'tags']