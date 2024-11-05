from flask import Flask
from config import Config
from models import db
from routes import api

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    from models import Task  # Import models
    db.create_all()  # Create tables

app.register_blueprint(api)  # Register API routes

if __name__ == '__main__':
    app.run(debug=True)
