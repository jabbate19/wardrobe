from flask import request, redirect, jsonify
from flask_login import login_user, logout_user, login_required
from ..models import User
from . import api_bp

@api_bp.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if user and user.authenticate(password):
        login_user(user)
        return 'OK', 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@api_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')
