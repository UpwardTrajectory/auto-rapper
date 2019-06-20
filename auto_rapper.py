

import json
import string
import lyricsgenius


if rappers is None:
    rappers = {}


def connect_to_genius(token=None):
    """
    use a 1 time token to connect to connect with genius api
    """

    if token is None:
        with open('./.secret/api_key.json') as f:
            temp_api = json.load(f)
            token = temp_api['token']
    return lyricsgenius.Genius(token)


def get_lyrics(artist, max_songs=None, json_folder='default'):
    """
    Search genius.com for {max_songs} songs by {artist} and return a
    dictionary of the {song_title : lyrics_as_single_string}. Optionally,
    save the dictionary as `artist.json` inside the path:
         json_folder='destination_folder_path'
    by default, will search for ALL available songs (sorted descending
    by popularity), and save them in `./artists/` folder
    """

    genius = connect_to_genius()

    current_artist = genius.search_artist(artist,
                                          max_songs=max_songs,
                                          get_full_info=False)

    artist_name = current_artist.name.lower().translate(
        str.maketrans('', '', string.punctuation)).replace(" ", "_")

    all_lyrics = {}

    for song in current_artist.songs:
        all_lyrics[song.title] = song.lyrics

    if json_folder is not None:
        if json_folder is 'default':
            json_folder = './artists/'

        json_folder += artist_name + '.json'

        with open(json_folder, 'w') as fp:
            json.dump(all_lyrics, fp)

    if all_lyrics not in rappers.values():
        rappers[artist_name] = all_lyrics
    return all_lyrics


def export_text(artist_name, artist_dict):
    """
    Take in a dictionary created by `get_lyrics()` and save a single corpus
    of their lyrics as a .txt file.
    """

    corpus = ""
    file = artist_name + '.txt'
    for text in artist_dict.values():
        corpus += text.replace('\n', ' \n ')
    path = 'artists/' + file

    try:
        with open(path, mode='x') as f:
            f.write(corpus)
    except FileExistsError:
        print('Already found ', file)

    return f'{file} saved to current folder'


class gpt2():
    
    __init__(self):
        pass


def test_print():
    return "test of a string output"

    