from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Spotify API credentials
SPOTIFY_CLIENT_ID = '4fae7b81aeba4167852828ec05725eb2'
SPOTIFY_CLIENT_SECRET = 'de4a888c3e274901bd01bc204de7e263'

# Function to get access token
def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    payload = {
        'grant_type': 'client_credentials'
    }
    
    try:
        response = requests.post(url, data=payload, auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()['access_token']
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")  # Log the error
        if response:
            print(f"Response: {response.text}")  # Log the response text for debugging
    except Exception as e:
        print(f"An error occurred: {e}")  # Log any other errors
    return None

# Route to search for sad songs based on a query from the frontend
@app.route('/search', methods=['POST'])  # Changed to POST
def search_sad_songs():
    # Get the search query from the request JSON
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "No search query provided"}), 400
    
    search_query = data['query']  # Extract the query from the JSON
    access_token = get_access_token()
    if access_token is None:
        return jsonify({"error": "Could not get access token"}), 401

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    url = f"https://api.spotify.com/v1/search?q={search_query}&type=track&limit=10"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tracks = response.json()['tracks']['items']
        sad_songs = []
        for track in tracks:
            song_info = {
                'id': track['id'],  # Include track ID
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'preview_url': track['preview_url'],
                'external_url': track['external_urls']['spotify']
            }
            sad_songs.append(song_info)

        return jsonify(sad_songs)
    else:
        return jsonify({"error": "Could not search for songs"}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
