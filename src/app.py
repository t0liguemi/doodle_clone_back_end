from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, User
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)

@app.route("/")
def home():
    return "Insert here your DOODLE CLONE APP"

if __name__ == '__main__':
    app.run(host="localhost", port=5000)