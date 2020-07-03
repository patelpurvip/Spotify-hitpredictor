from pickle import load
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import pandas as pd
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
    print(spotify)

    try:
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
        x = [[f['danceability'],
            f['energy'],
            f['key'],
            f['loudness'],
            f['mode'],
            f['speechiness'],
            f['acousticness'],
            f['instrumentalness'],
            f['liveness'],
            f['valence'],
            f['tempo'],
            f['duration_ms'],
            f['time_signature'],
            chorus_hit,
            count_sections]]
        
        # Create dataframe of data
        table = pd.DataFrame({
            'danceability': [f['danceability']],
            'energy': [f['energy']],
            'key': [f['key']],
            'loudness': [f['loudness']],
            'mode': [f['mode']],
            'speechiness': [f['speechiness']],
            'acousticness': [f['acousticness']],
            'instrumentalness': [f['instrumentalness']],
            'liveness': [f['liveness']],
            'valence': [f['valence']],
            'tempo': [f['tempo']],
            'duration_ms': [f['duration_ms']],
            'time_signature': [f['time_signature']],
            'chorus_hit': [chorus_hit],
            'count_sections': [count_sections]
            })
        ttable = table.T
        feature_table = ttable.to_html(classes="table table-hover table-success table-striped", 
            justify='center',
            header=False)

        # Scaling data
        x_scaled = scaler.transform(x)

        # Running model
        hit_predict = model.predict(x_scaled)
        hit_score = model.predict_proba(x_scaled)

        return [hit_predict, hit_score, feature_table]
    
    except:
        error = "We can't find your entry in the spotify database, please check your spelling and/or try again"
        return [error]
