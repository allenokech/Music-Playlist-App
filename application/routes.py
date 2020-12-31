from application import app, db
from application.models import Song, Playlist, PlaylistSong
from application.forms import SongForm, PlaylistForm

from flask import render_template, request, redirect, url_for, redirect

@app.route('/')
@app.route('/home')
def home():
    all_playlists = Playlist.query.all()
    
    return render_template("index.html", title="Home", all_playlists=all_playlists)

@app.route('/view/<int:playlist_id>', methods=['GET'])
def view_playlist(playlist_id):
    playlist = Playlist.query.get(id)

    return render_template('view.html', playlist=playlist)

@app.route('/addsong/<int:song_id>', methods=['GET','POST'])
def addsong():
    form = SongForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_song = Songs(form.title.data, form.artist_name.data)
            db.session.add(new_song)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("addsong.html", title="Add a Song", form=form)

@app.route('/create', methods=['GET','POST'])
def create_playlist():
    form = PlaylistForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_playlist = Playlist(playlist_name=form.name.data)
            db.session.add(create_playlist)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('newplaylist.html', title='Create a playlist', form=form)

@app.route('/update/<int:id>', methods=['GET','POST'])
def update_playlist(id):
    form = PlaylistForm()
    playlist = Playlist.query.filter_by(id=id).first()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_playlist = Playlist(playlist_name=form.name.data)
            db.session.add(create_playlist)
            db.session.commit()
            return redirect(url_for("home"))

@app.route('/delete/<int:id>', methods=['GET','POST'])
def delete_playlist(id):
    playlist = Playlist.query.filter_by(id=id).first()
    db.session.delete(playlist)
    db.session.commit()
    return redirect(url_for("home"))
