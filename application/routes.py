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

@app.route('/create', methods=['GET','POST'])
def create_playlist():
    form = PlaylistForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_playlist = Playlist(form.playlist_name)
            db.session.add(create_playlist)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('create.html', title='Create a playlist', form=form)

@app.route('/addsong/<int:playlist_id>', methods=['GET','POST'])
def addsong(playlist_id):
    form = SongForm()
    all_songs = Song.query.filter_by(playlist_id=id).all()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_song = Songs(song_title=form.song_title.data, playlist_id=id)
            db.session.add(new_song)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("addsong.html", title="Add a Song", form=form)

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    form = PlaylistForm()
    updateplaylist = Playlist.query.filter_by(id=id).first()
    if request.method == 'POST':
        playlist.playlist_name = form.playlist_name.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Update Playlist", playlist=playlist)

@app.route('/delete/<int:id>')
def delete(id):
    deleteplaylist = Playlist.query.filter_by(id=id).first()
    db.session.delete(deleteplaylist)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/deletesong/<int:id>')
def deletesong(id):
    deletesong = Song.query.filter_by(id=id).first()
    db.session.delete(deletesong)
    db.session.commit()
    return redirect(url_for("home"))