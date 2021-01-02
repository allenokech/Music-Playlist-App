from application import app, db
from application.models import Song, Playlist, association_table
from application.forms import SongForm, PlaylistForm
from flask import render_template, request, redirect, url_for

@app.route('/')
@app.route('/home')
def home():
    all_playlists = Playlist.query.all()
    all_songs = Song.query.all()
    return render_template("index.html", title="Home", all_playlists=all_playlists, all_songs=all_songs)

@app.route('/view/<int:id>')
def view_playlist(id):
    playlist = Playlist.query.all()
    playlist = Playlist.query.get(id)

    return render_template('view.html', playlist=playlist)

@app.route('/create', methods=['GET','POST'])
def create_playlist():
    form = PlaylistForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_playlist = Playlist(playlist_name=form.playlist_name.data)
            db.session.add(new_playlist)
            db.session.commit()
            return redirect(url_for("home"))
    
    return render_template('create.html', title='Create a playlist', form=form)

@app.route('/addsong', methods=['GET','POST'])
def addsong():
    form = SongForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_song = Song(song_title=form.song_title.data)
            db.session.add(new_song)
            db.session.commit()
            return redirect(url_for("home"))
    
    return render_template("add.html", title="Add a Song", form=form)

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    form = PlaylistForm()
    playlist = Playlist.query.filter_by(id=id).first()
    if request.method == 'POST':
        playlist.playlist_name = form.playlist_name.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Updated Playlist", playlist=playlist)

@app.route('/delete/<int:id>')
def delete(id):
    playlist = Playlist.query.filter_by(id=id).first()
    db.session.delete(playlist)
    db.session.commit()
    return redirect(url_for("home"))