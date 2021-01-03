from application import db
from datetime import datetime
from sqlalchemy.orm import backref
  
class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_name = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    song = db.relationship('Song', backref='theplaylist', lazy=True)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.relationship(Playlist)
    song_title = db.Column(db.String(50), nullable=False)
    artist_name = db.Column(db.String(50), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    playlist = db.Column(db.Integer, db.ForeignKey('playlist.id'), nullable=False)

#association_table = db.Table('association_table', db.Model.metadata,
 #   db.Column('playlist_id', db.Integer, db.ForeignKey('playlist.id')),
  #  db.Column('song_id', db.Integer, db.ForeignKey('song.id')))


#class PlaylistSong():
 #   playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
  #  song_id = db.Column(db.Integer, db.ForeignKey('song.id'))