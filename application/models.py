from datetime import datetime
from application import db

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(50), nullable=False)
    song_title = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
 #   playlistsong = db.relationship('playlistsong', backref='song')

association_table = db.Table('association_table', db.Model.metadata,
    db.Column('playlist', db.Integer, db.ForeignKey('playlist.id')),
    db.Column('song_id', db.Integer, db.ForeignKey('song.id')))

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    songs = db.relationship('Song', secondary='association_table', backref='playlist')





#class PlaylistSong():
 #   playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
  #  song_id = db.Column(db.Integer, db.ForeignKey('song.id'))