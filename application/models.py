from datetime import datetime
from application import db

association_table = db.Table('playlist_song', db.Model.metadata,
    db.Column('song_id', db.Integer, db.foreign_key('song.id')),
    db.Column('playlist_id', db.Integer, db.foreign_key('playlist.id')),
)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(30, nullable=False))
    title = db.Column(db.String(30, nullable=False))
    genre = db.Column(db.String(30, nullable=False))
    release_year = db.Column(db.Integer, nullable=False)
    playlist = db.relationship('Playlist', secondary='playlist_song', backref='song')

class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.String(30, nullable=False))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
