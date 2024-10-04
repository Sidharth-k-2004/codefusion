from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

app = Flask(__name__)
CORS(app)  # Enable CORS

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/yourDatabase"
mongo = PyMongo(app)

# Signup route
@app.route('/signup', methods=['POST'])
def signup():
    try:
        username = request.json['username']
        password = request.json['password']

        # Check if the user already exists
        existing_user = mongo.db.users.find_one({'username': username})
        if existing_user:
            return jsonify({'message': 'User already exists.'}), 400

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        # Create a new user
        mongo.db.users.insert_one({
            'username': username,
            'password': hashed_password,
            'selectedLanguages': [],
            'selectedArtists': []
        })

        return jsonify({'message': 'Signup successful!'}), 200
    except Exception as error:
        print(error)
        return jsonify({'message': 'An error occurred during signup.'}), 500


# Login route
@app.route('/login', methods=['POST'])
def login():
    try:
        username = request.json['username']
        password = request.json['password']

        # Check if user exists
        user = mongo.db.users.find_one({'username': username})
        if not user:
            return jsonify({'message': 'User not found.'}), 400

        # Compare passwords
        if not bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return jsonify({'message': 'Incorrect password.'}), 400

        return jsonify({'message': 'Login successful!', 'userId': str(user['_id'])}), 200
    except Exception as error:
        print(error)
        return jsonify({'message': 'An error occurred during login.'}), 500


# Store user selections route
@app.route('/storeSelection', methods=['POST'])
def store_selection():
    try:
        user_id = request.json['userId']
        selected_languages = request.json['selectedLanguages']
        selected_artists = request.json['selectedArtists']

        # Update the user with their selected languages and artists
        mongo.db.users.update_one(
            {'_id': ObjectId(user_id)},  # Find the user by their ID
            {'$set': {'selectedLanguages': selected_languages, 'selectedArtists': selected_artists}}  # Update their selections
        )

        return jsonify({'message': 'Selections saved successfully!'}), 200
    except Exception as error:
        print(error)
        return jsonify({'message': 'An error occurred while saving selections.'}), 500


# Start the server
if __name__ == '__main__':
    app.run(port=5000,host='0.0.0.0')
