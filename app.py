import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of Music Albums and Playlists.</p>'''

#Get all media types
@app.route('/api/v1/resources/media/all', methods=['GET'])
def api_media_all():
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_media = cur.execute('SELECT * FROM media_types;').fetchall()

    return jsonify(all_media)

#Get all genres types
@app.route('/api/v1/resources/genres/all', methods=['GET'])
def api_genres_all():
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    genres = cur.execute('SELECT * FROM genres;').fetchall()

    return jsonify(genres)    

#Get all playlists types
@app.route('/api/v1/resources/playlists/all', methods=['GET'])
def api_playlists_all():
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    playlists = cur.execute('SELECT * FROM playlists;').fetchall()

    return jsonify(playlists)

#Get all playlist_track types
@app.route('/api/v1/resources/playlist_track/all', methods=['GET'])
def api_playlist_track_all():
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    playlist_track = cur.execute('SELECT * FROM playlist_track;').fetchall()

    return jsonify(playlist_track)    

#Get all tracks types
@app.route('/api/v1/resources/tracks/all', methods=['GET'])
def api_tracks_all():
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    tracks = cur.execute('SELECT * FROM tracks;').fetchall()

    return jsonify(tracks) 
#Get all artists types
@app.route('/api/v1/resources/artists/all', methods=['GET'])
def api_artists_all():
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    artists = cur.execute('SELECT * FROM artists;').fetchall()

    return jsonify(artists)

#Get all albums types
@app.route('/api/v1/resources/albums/all', methods=['GET'])
def api_albums_all():
    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    albums = cur.execute('SELECT * FROM albums;').fetchall()

    return jsonify(albums)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/tracks', methods=['GET'])
def api_filter():
    query_parameters = request.args

    trackid = query_parameters.get('TrackId')
    name = query_parameters.get('Name')
    albumid = query_parameters.get('AlbumId')
    composer = query_parameters.get('Composer')

    query = "SELECT * FROM tracks WHERE"
    to_filter = []

    if trackid:
        query += ' trackid=? AND'
        to_filter.append(trackid)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if albumid:
        query += ' albumid=? AND'
        to_filter.append(albumid)
    if composer:
        query += ' composer=? AND'
        to_filter.append(composer)    
    if not (trackid or name or albumid or composer):
        return page_not_found(404)

    query = query[:-4] + ';'

    conn = sqlite3.connect('chinook.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

app.run()
