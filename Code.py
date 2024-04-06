import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    return pd.read_json(file_path)

def clean_data(dataset):
    dataset['endTime'] = pd.to_datetime(dataset['endTime'])
    dataset['msPlayed'] = pd.to_numeric(dataset['msPlayed'], errors='coerce')
    return dataset

def extract_top_artists(dataset, n=10):
    return dataset['artistName'].value_counts().head(n)

def plot_top_artists(top_artists):
    plt.figure(figsize=(10, 6))
    top_artists.plot(kind='bar')
    plt.title('Top Ten Most Listened to Artists')
    plt.xlabel('Artist')
    plt.ylabel('Number of Listens')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def save_top_artists_csv(top_artists, file_name):
    top_artists.to_csv(file_name, index=False)

def extract_top_songs(dataset, n=10):
    top_songs = dataset.groupby(['artistName', 'trackName']).size().reset_index(name='listens')
    return top_songs.sort_values(by='listens', ascending=False).head(n)

def plot_top_songs(top_songs):
    plt.figure(figsize=(10, 6))
    top_songs.plot(kind='bar', x='trackName', y='listens')
    plt.title('Top Ten Most Listened to Songs')
    plt.xlabel('Song')
    plt.ylabel('Number of Listens')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def calculate_total_listening_time(dataset):
    total_time_ms = dataset['msPlayed'].sum()
    total_time_min = total_time_ms / (1000 * 60)
    total_time_hr = total_time_min / 60
    return total_time_min, total_time_hr

def analyze_favorite_artist(dataset, favorite_artist):
    top_songs_favorite = dataset[dataset['artistName'] == favorite_artist].groupby('trackName').size().reset_index(name='listens')
    return top_songs_favorite.sort_values(by='listens', ascending=False).head(10)

def plot_favorite_artist_songs(top_songs_favorite, artist_name):
    plt.figure(figsize=(10, 6))
    top_songs_favorite.plot(kind='bar', x='trackName', y='listens')
    plt.title(f'Top Songs of {artist_name}')
    plt.xlabel('Song')
    plt.ylabel('Number of Listens')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def analyze_artist_trends(dataset, artist_name):
    favorite_artist_trends = dataset[dataset['artistName'] == artist_name].copy()
    favorite_artist_trends.loc[:, 'date'] = favorite_artist_trends['endTime'].dt.date
    return favorite_artist_trends.groupby('date').size().reset_index(name='listens')

def plot_artist_trends(trends, artist_name):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='listens', data=trends)
    plt.title(f'Trends in Listening to {artist_name}')
    plt.xlabel('Date')
    plt.ylabel('Number of Listens')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def analyze_song_trends(dataset, song_name):
    favorite_song_trends = dataset[dataset['trackName'] == song_name].copy()
    favorite_song_trends.loc[:, 'date'] = favorite_song_trends['endTime'].dt.date
    return favorite_song_trends.groupby('date').size().reset_index(name='listens')

def plot_song_trends(trends, song_name):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='date', y='listens', data=trends)
    plt.title(f'Trends of {song_name} Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Listens')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Example usage
file_path = r'c:\Users\Asus\Spotify Data Analysis\StreamingHistory_music_0.json'
dataset = load_data(file_path)
dataset = clean_data(dataset)

top_artists = extract_top_artists(dataset)
plot_top_artists(top_artists)
save_top_artists_csv(top_artists, 'top_artists.csv')

top_songs = extract_top_songs(dataset)
plot_top_songs(top_songs)

total_time_min, total_time_hr = calculate_total_listening_time(dataset)
print(f"Total Listening Time: {total_time_min} mins / {total_time_hr} hrs")

favorite_artist = 'Lauren Jauregui'
top_songs_favorite = analyze_favorite_artist(dataset, favorite_artist)
plot_favorite_artist_songs(top_songs_favorite, favorite_artist)

favorite_artist_trends = analyze_artist_trends(dataset, favorite_artist)
plot_artist_trends(favorite_artist_trends, favorite_artist)

favorite_song = 'Headaches'
trends_song = analyze_song_trends(dataset, favorite_song)
plot_song_trends(trends_song, favorite_song)
