Music Recommender System
Overview
This Music Recommender System provides song recommendations based on user input. Utilizing a pre-trained similarity model and the Spotify API, the application recommends songs and displays their album covers. It's built using Python and Streamlit for the web interface.
Features
* Song Recommendations: Get personalized song recommendations.
* Album Covers: Displays album covers of recommended songs using the Spotify API.
* Interactive Interface: User-friendly interface built with Streamlit.
Setup
Follow these steps to set up and run the Music Recommender System on your local machine:

1 Clone the Repository
git clone https://github.com/Kalyankumarmohanbabu/music-recommendation-system 

2 Install Dependencies
Make sure you have Python installed. It's recommended to use a virtual environment.
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

3 Set Up Spotify API Credentials
* Create an application on the Spotify Developer Dashboard.
* Obtain your Client ID and Client Secret.
* Set environment variables for your Spotify API credentials:

export SPOTIPY_CLIENT_ID='your_client_id'
export SPOTIPY_CLIENT_SECRET='your_client_secret'

4 Place Data Files
Ensure the following pickle files are placed in the project directory:

1.df.pkl
2.similarity.pkl

3.Usage
Run the Streamlit app:
streamlit run app.py

5.License
This project is licensed under the MIT License.
