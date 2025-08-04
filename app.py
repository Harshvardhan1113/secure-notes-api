from notes import notes
from flask import Flask
from flask_cors import CORS
from models import db
from auth import auth

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key'

# Initialize extensions
CORS(app)
db.init_app(app)
app.register_blueprint(auth)
app.register_blueprint(notes)  # ✅ Only here!

# Root route
@app.route('/')
def home():
    return " Secure Notes API is running!"

# Create DB tables only when running the app directly
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
