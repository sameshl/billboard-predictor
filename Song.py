import pandas as pd
# from pprint import pprint

import spotipy
import spotipy.util as util
from load import get_standard_scalar

# Import StandardScaler object with transformed values
sc = get_standard_scalar()


class Song:
    """Class for song features from spotify"""

    def __init__(self, artist, song, choice):

        self.artist = artist
        self.song = song
        self.choice = choice
        self.artist_score = self.get_artist_score()

    def get_artist_score(self):
        """Determine the artist score by choice"""
        if self.choice == 'Yes':
            return 1
        elif self.choice == 'No':
            return 0
        else:
            return 0.5

    @staticmethod
    def authenticate():
        """Authenticate with spotify api"""
        token = util.oauth2.SpotifyClientCredentials(
            client_id='578d6e7b02e3421c903fa7794aab9118',
            client_secret='b610ff6ee28b4b359098b97e384d7637')
        cache_token = token.get_access_token()
        # spotify = spotipy.Spotify(cache_token)
        sp = spotipy.Spotify(auth=cache_token)
        # print('Authenticated')
        return sp

    @property
    def song_features(self):
        """Get the spotify data for given song, artist"""

        sp = self.authenticate()
        try:
            self.track_info = sp.search(q='artist:' + self.artist + ' track:' +
                                        self.song,
                                        type='track')
            # pprint(self.track_info)
            track_id = self.track_info['tracks']
            track_id2 = track_id['items']
            if track_id2 != []:
                year = self.track_info['tracks']
                year_1 = year['items']
                year_2 = year_1[0]
                year_3 = year_2['album']
                year_4 = year_3['release_date']
                year_5 = year_4.split('-')
                if len(year_5) > 1:
                    # year_6 = year_5[0]
                    track_id3 = track_id2[0]
                    track_id4 = track_id3['id']
                    # month = year_5[1]
                    feat_t = sp.audio_features(tracks=track_id4)
                    # pprint(feat_t)
                    feat = feat_t[0]

                    danceability = feat['danceability']
                    energy = feat['energy']
                    key = feat['key']
                    loudness = feat['loudness']
                    mode = feat['mode']
                    speechiness = feat['speechiness']
                    acousticness = feat['acousticness']
                    instrumentalness = feat['instrumentalness']
                    liveness = feat['liveness']
                    valence = feat['valence']
                    tempo = feat['tempo']
            self.features = {'danceability': danceability,
                             'energy': energy,
                             'key': key,
                             'loudness': loudness,
                             'mode': mode,
                             'speechiness': speechiness,
                             'acousticness': acousticness,
                             'instrumentalness': instrumentalness,
                             'liveness': liveness,
                             'valence': valence,
                             'tempo': tempo,
                             'artist_score': self.artist_score}
            # print(features)
            return self.features
        except Exception as e:
            print('Could not get data for', self.song, 'by', self.artist,
                  'Error:', e)

    @song_features.setter
    def song_features(self, features):
        self.features = features

    def clean_features(self):
        """Clean the data from spotify"""
        data = pd.DataFrame([self.song_features])

        # Make temporary data to match shape of dataframe in machine learning
        # model
        for i in range(0, 12):
            if i % 2 == 0:
                j = 0
            else:
                j = 1
            temp = {'danceability': 0.8, 'energy': 0.7, 'key': i,
                    'loudness': -3, 'mode': j,
                    'speechiness': 0.08, 'acousticness': 0.6,
                    'instrumentalness': 0,
                    'liveness': 0.09, 'valence': 0.9, 'tempo': 96,
                    'artist_score': 0}

            data = data.append(temp, ignore_index=True)
        cols = ['danceability', 'energy', 'key', 'loudness', 'mode',
                'speechiness',
                'acousticness', 'instrumentalness', 'liveness', 'valence',
                'tempo',
                'artist_score']
        data = data[cols]
        mode = pd.get_dummies(data['mode'], drop_first=True)
        key = pd.get_dummies(data['key'], drop_first=True)
        data.drop(['mode', 'key'], axis=1, inplace=True)
        data = pd.concat([data, mode, key], axis=1)
        # Dropping all other temporary rows before using StandardScaler
        data.drop(data.index[1:], inplace=True)
        data = sc.transform(data)
        return data

    @property
    def data(self):
        """Get machine learning model ready data"""
        return self.clean_features()

    def extract_trackinfo(self):
        _ = self.song_features
        self.song_info()
        # pprint(self.track_info)

    def song_info(self):
        """Extract extra song info from track_info"""
        item = self.track_info['tracks']['items'][0]
        self.song_name = item['name']
        self.artist_name = item['artists'][0]['name']
        self.song_url = item['external_urls']['spotify']
        self.popularity = item['popularity']
        self.preview_url = item['preview_url']
        self.preview_img_urls = item['album']['images'][0]['url']
        print(self.song_name, self.artist_name, self.song_url,
              self.popularity, self.preview_url, self.preview_img_urls)


if __name__ == '__main__':
    user_song = Song(artist='the chainsmokers', song='Closer', choice='Yes')
    # user_song.data
    user_song.extract_trackinfo()
