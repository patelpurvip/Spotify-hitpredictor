from pickle import load
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import pandas as pd
import os

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
        
        
        
        
        key = ''
        mode = ''

        if f['mode'] == 1:
            mode = 'Major'
        else:
            mode = 'Minor'

        if f['key']

        # Create dataframe of data
        table = pd.DataFrame({
            'Danceability': [f['danceability']],
            'Energy': [f['energy']],
            'Key': [key],
            'Loudness': [f['loudness']],
            'Mode': [mode],
            'Speechiness': [f['speechiness']],
            'Acousticness': [f['acousticness']],
            'Instrumentalness': [f['instrumentalness']],
            'Liveness': [f['liveness']],
            'Valence': [f['valence']],
            'Tempo': [f['tempo']],
            'Duration in seconds': [f['duration_ms']/1000],
            'Time Signature': [f['time_signature']],
            'Aprox time the chorus "hit"': [chorus_hit],
            'Sections count': [count_sections]
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
