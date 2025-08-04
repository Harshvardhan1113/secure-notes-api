from flask import Blueprint, request, jsonify, current_app
from models import db, Note
import jwt
from functools import wraps


notes = Blueprint('notes', __name__)


# Middleware to check JWT token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user_id = data['user_id']
        except Exception as e:
            return jsonify({'message': 'Token is invalid or expired!', 'error': str(e)}), 401

        return f(current_user_id, *args, **kwargs)

    return decorated


# POST /notes - create a note
@notes.route('/notes', methods=['POST'])
@token_required
def create_note(current_user_id):
    data = request.get_json()
    content = data.get('content')

    if not content:
        return jsonify({"message": "Note content is required"}), 400

    new_note = Note(content=content, user_id=current_user_id)
    db.session.add(new_note)
    db.session.commit()
    return jsonify({"message": "Note created!"}), 201


# GET /notes - get all notes for current user
@notes.route('/notes', methods=['GET'])
@token_required
def get_notes(current_user_id):
    notes = Note.query.filter_by(user_id=current_user_id).all()
    return jsonify([{"id": note.id, "content": note.content} for note in notes]), 200


# DELETE /notes/<id> - delete a note
@notes.route('/notes/<int:note_id>', methods=['DELETE'])
@token_required
def delete_note(current_user_id, note_id):
    note = Note.query.filter_by(id=note_id, user_id=current_user_id).first()

    if not note:
        return jsonify({"message": "Note not found"}), 404

    db.session.delete(note)
    db.session.commit()
    return jsonify({"message": "Note deleted!"}), 200
