import os
import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Directly set the environment variables within the script
os.environ['SPOTIPY_CLIENT_ID'] = 'b8b08b35ce114e6e927fc258d6f739bd'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'c04d2769dc134d93991b00d14b3b9dbb'

# Load environment variables
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

if not CLIENT_ID or not CLIENT_SECRET:
    st.error("Spotify client ID and secret must be set in environment variables.")
    st.stop()

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    try:
        search_query = f"track:{song_name} artist:{artist_name}"
        results = sp.search(q=search_query, type="track")

        if results and results["tracks"]["items"]:
            track = results["tracks"]["items"][0]
            album_cover_url = track["album"]["images"][0]["url"]
            return album_cover_url
        else:
            return "https://i.postimg.cc/0QNxYz4V/social.png"
    except Exception as e:
        st.error(f"Error fetching album cover: {e}")
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(song):
    try:
        index = music[music['song'] == song].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_music_names = []
        recommended_music_posters = []
        for i in distances[1:6]:
            # fetch the music poster
            artist = music.iloc[i[0]].artist
            recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
            recommended_music_names.append(music.iloc[i[0]].song)

        return recommended_music_names, recommended_music_posters
    except IndexError:
        st.error("Song not found in the dataset.")
        return [], []
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return [], []

st.header('Music Recommender System')
try:
    music = pickle.load(open(r'D:\music rec\df.pkl', 'rb'))
    similarity = pickle.load(open(r'D:\music rec\similarity.pkl', 'rb'))
except FileNotFoundError:
    st.error("Data files not found. Please check the path and try again.")
    st.stop()
except pickle.UnpicklingError as e:
    st.error(f"Error loading pickle files: {e}")
    st.stop()

music_list = music['song'].values
selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommended_music_names, recommended_music_posters = recommend(selected_song)
    num_recommendations = len(recommended_music_names)
    if num_recommendations > 0:
        cols = st.columns(min(num_recommendations, 5))
        for i in range(num_recommendations):
            with cols[i]:
                st.text(recommended_music_names[i])
                st.image(recommended_music_posters[i])
    else:
        st.write("No recommendations found.")
