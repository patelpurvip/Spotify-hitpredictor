from pickle import load
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

# # test data
# track = "black parade"
# artist = "Beyoncé"

def hit_flop(track, artist):

    # Load model
    model = load(open('model.pkl', 'rb'))
    scaler = load(open('scaler.pkl', 'rb'))

    # Load keys
    load_dotenv()
    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

    # Transform strings to lower case
    track = track.lower()
    artist = artist.lower()

    # Call song
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    results = spotify.search(q='track:' + track, type='track')

    # Find song uri by matching artist
    items = results['tracks']['items']
    for i in items:
        item_artist = i['artists'][0]['name']
        if item_artist.lower() == artist:
            uri = i['uri']

    # Setting information from audio analysis
    audio_analysis = spotify.audio_analysis(track_id=uri)
    count_sections = len(audio_analysis['sections'])
    chorus_hit = audio_analysis['sections'][2]['start']
    
    # Setting information from audio features
    audio_features = spotify.audio_features(tracks=[uri])
    f = audio_features[0]

    # Arrange data to load to model
    x = [[f['danceability'],f['energy'],f['key'],f['loudness'],f['mode'],f['speechiness'],f['acousticness'],f['instrumentalness'],f['liveness'],f['valence'],f['tempo'],f['duration_ms'],f['time_signature'],chorus_hit,count_sections]]

    # Scaling data
    x_scaled = scaler.transform(x)

    # Running model
    hit_predict = model.predict(x_scaled)
    hit_score = model.predict_proba(x_scaled)

    return hit_predict, hit_score