from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

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
        print(f"Response: {response.text}")  # Log the response text for debugging
    except Exception as e:
        print(f"An error occurred: {e}")  # Log any other errors
    return None

# Route to search for sad songs by Arijit Singh
@app.route('/search/sad-songs', methods=['GET'])
def search_sad_songs():
    access_token = get_access_token()
    if access_token is None:
        return jsonify({"error": "Could not get access token"}), 401

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    search_query = "melody songs"
    url = f"https://api.spotify.com/v1/search?q={search_query}&type=track&limit=10"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tracks = response.json()['tracks']['items']
        sad_songs = []
        for track in tracks:
            song_info = {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'preview_url': track['preview_url'],
                'external_url': track['external_urls']['spotify']
            }
            sad_songs.append(song_info)

        return jsonify(sad_songs)
    else:
        return jsonify({"error": "Could not search for songs"}), 500
    
# Function to get recommendations based on mood
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    access_token = get_access_token()
    if access_token is None:
        return jsonify({"error": "Could not get access token"}), 401

    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    mood = request.args.get('mood', 'sad')  # Default to 'sad'
    
    # Spotify uses 'valence' (happiness), 'energy', etc. to classify mood
    # For 'sad' songs, we'll aim for lower valence, lower energy
    url = f"https://api.spotify.com/v1/recommendations?limit=10&seed_genres=pop&min_valence=0.1&max_valence=0.4&min_energy=0.1&max_energy=0.6"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tracks = response.json()['tracks']
        recommendations = []
        for track in tracks:
            song_info = {
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'preview_url': track['preview_url'],
                'external_url': track['external_urls']['spotify']
            }
            recommendations.append(song_info)

        return jsonify(recommendations)
    else:
        return jsonify({"error": "Could not get recommendations"}), 500


if __name__ == "__main__":
    app.run(port=5000, debug=True)
