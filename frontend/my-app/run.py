from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId  # Import ObjectId for MongoDB
import bcrypt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Connect to MongoDB
client = MongoClient('mongodb+srv://sidharthkdinesan123:MuiiFKdawTLot40o@kcet-resukts.t7dnjbg.mongodb.net/?retryWrites=true&w=majority&appName=kcet-resukts')
db = client['kcet_database']  
users_collection = db['users']  
username=0

# Signup route
@app.route('/signup', methods=['POST'])
def signup():
    try:
        username = request.json['username']
        password = request.json['password']

        print(f"Attempting to register user: {username}")

        if users_collection.find_one({'username': username}):
            print(f"Username '{username}' already exists.")
            return jsonify({'error': 'Username already exists'}), 400

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        new_user = {
            'username': username,
            'password': hashed_password
        }
        
        users_collection.insert_one(new_user)
        print(f"User '{username}' registered successfully.")

        return jsonify({'message': 'User registered successfully'}), 201

    except Exception as e:
        print("Error occurred during signup:", e)  # Log the full error
        return jsonify({'error': 'An error occurred during signup.'}), 500

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    user = users_collection.find_one({'username': username})

    if user:
        if bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    else:
        return jsonify({'error': 'User not found'}), 404

# Store selections route
@app.route('/storeSelection', methods=['POST'])
def store_selection():
    try:
        data = request.json
        # user_id = data['userId']
        user_id=username
        selected_languages = data['selectedLanguages']
        selected_artists = data['selectedArtists']

        # Convert user_id to ObjectId if necessary
        if not ObjectId.is_valid(user_id):
            return jsonify({'error': 'Invalid user ID format'}), 400
        user_id = ObjectId(user_id)

        # Update the user with their selected languages and artists
        result = users_collection.update_one(
            {'_id': user_id},  # Find the user by their ID
            {'$set': {
                'selectedLanguages': selected_languages,
                'selectedArtists': selected_artists
            }}
        )

        if result.modified_count > 0:
            return jsonify({'message': 'Selections saved successfully!'}), 200
        else:
            return jsonify({'message': 'No changes made or user not found.'}), 404

    except Exception as error:
        print("Error occurred:", error)  # Log the full error
        return jsonify({'message': 'An error occurred while saving selections.', 'error': str(error)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
