from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired
from application.models import Playlist, Song

class SongForm(FlaskForm):
    song_title = StringField("Song Title", validators=[DataRequired()])
    artist_name = StringField("Artist's Name", validators=[DataRequired()])
    genre = StringField("Song Genre", validators=[DataRequired()])
    release_year = IntegerField("Year of Release", validators=[DataRequired()])
    playlist = SelectField("Select Playlist", choices=[(p.id, p.playlist_name) for p in Playlist.query.order_by("playlist_name") ])
    submit = SubmitField("Add Song")

class PlaylistForm(FlaskForm):
    playlist_name = StringField("Name of the Playlist", validators=[DataRequired()]) 
    submit = SubmitField("Create Playlist")