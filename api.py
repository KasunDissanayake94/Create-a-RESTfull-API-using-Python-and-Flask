import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
tracks = [
  {
    "AlbumId": 1, 
    "Bytes": 11170334, 
    "Composer": "Angus Young, Malcolm Young, Brian Johnson", 
    "GenreId": 1, 
    "MediaTypeId": 1, 
    "Milliseconds": 343719, 
    "Name": "For Those About To Rock (We Salute You)", 
    "TrackId": 1, 
    "UnitPrice": 0.99
  }, 
  {
    "AlbumId": 2, 
    "Bytes": 5510424, 
    "Composer": "Angus Young, Malcolm Young, Brian Johnson", 
    "GenreId": 1, 
    "MediaTypeId": 2, 
    "Milliseconds": 342562, 
    "Name": "Balls to the Wall", 
    "TrackId": 2, 
    "UnitPrice": 0.99
  }, 
  {
    "AlbumId": 3, 
    "Bytes": 3990994, 
    "Composer": "F. Baltes, S. Kaufman, U. Dirkscneider & W. Hoffman", 
    "GenreId": 1, 
    "MediaTypeId": 2, 
    "Milliseconds": 230619, 
    "Name": "Fast As a Shark", 
    "TrackId": 3, 
    "UnitPrice": 0.99
  }, 
  {
    "AlbumId": 3, 
    "Bytes": 4331779, 
    "Composer": "F. Baltes, R.A. Smith-Diesel, S. Kaufman, U. Dirkscneider & W. Hoffman", 
    "GenreId": 1, 
    "MediaTypeId": 2, 
    "Milliseconds": 252051, 
    "Name": "Restless and Wild", 
    "TrackId": 4, 
    "UnitPrice": 0.99
  }, 
  {
    "AlbumId": 3, 
    "Bytes": 6290521, 
    "Composer": "Deaffy & R.A. Smith-Diesel", 
    "GenreId": 1, 
    "MediaTypeId": 2, 
    "Milliseconds": 375418, 
    "Name": "Princess of the Dawn", 
    "TrackId": 5, 
    "UnitPrice": 0.99
  }, 
  {
    "AlbumId": 1, 
    "Bytes": 6713451, 
    "Composer": "Angus Young, Malcolm Young, Brian Johnson", 
    "GenreId": 1, 
    "MediaTypeId": 1, 
    "Milliseconds": 205662, 
    "Name": "Put The Finger On You", 
    "TrackId": 6, 
    "UnitPrice": 0.99
  }, 
  {
    "AlbumId": 1, 
    "Bytes": 7636561, 
    "Composer": "Angus Young, Malcolm Young, Brian Johnson", 
    "GenreId": 1, 
    "MediaTypeId": 1, 
    "Milliseconds": 233926, 
    "Name": "Let's Get It Up", 
    "TrackId": 7, 
    "UnitPrice": 0.99
  }, 
  {
    "AlbumId": 1, 
    "Bytes": 6852860, 
    "Composer": "Angus Young, Malcolm Young, Brian Johnson", 
    "GenreId": 1, 
    "MediaTypeId": 1, 
    "Milliseconds": 210834, 
    "Name": "Inject The Venom", 
    "TrackId": 8, 
    "UnitPrice": 0.99
  }, 
  {
    "AlbumId": 1, 
    "Bytes": 6599424, 
    "Composer": "Angus Young, Malcolm Young, Brian Johnson", 
    "GenreId": 1, 
    "MediaTypeId": 1, 
    "Milliseconds": 203102, 
    "Name": "Snowballed", 
    "TrackId": 9, 
    "UnitPrice": 0.99
  }, 
  {
    "AlbumId": 1, 
    "Bytes": 8611245, 
    "Composer": "Angus Young, Malcolm Young, Brian Johnson", 
    "GenreId": 1, 
    "MediaTypeId": 1, 
    "Milliseconds": 263497, 
    "Name": "Evil Walks", 
    "TrackId": 10, 
    "UnitPrice": 0.99
  }
    
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to New Project</h1>

<p>A prototype API for distant reading of Music Albums and Playlists.</p>'''

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/tracks/all', methods=['GET'])
def api_all():
    return jsonify(tracks)

@app.route('/api/v1/resources/tracks', methods=['GET'])
def api_id():
    
    #Check ID and If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Empty List
    results = []

    # Check trackid in catalog and return the result
    for track in tracks:
        if track['TrackId'] == id:
            results.append(track)

    # Convert our list of python dictionaries to the JSON format.
    return jsonify(results)

app.run()

