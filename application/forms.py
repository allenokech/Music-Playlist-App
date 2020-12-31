from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SongForm(FlaskForm):
    artist_name = StringField("Artist's Name", validators=[DataRequired()])
    song_title = StringField("Song Title", validators=[DataRequired()])
    genre = StringField("Song Genre", validators=[DataRequired()])
    release_year = StringField("Year of Release", validators=[DataRequired()])
    submit = SubmitField("Add Song")

class PlaylistForm(FlaskForm):
    playlist_name = StringField("Name of the Playlist", validators=[DataRequired()])
    submit = SubmitField("Create Playlist")