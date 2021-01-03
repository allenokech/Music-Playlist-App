import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Playlist, Song

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True
        )
        return app

    def setUp(self):
        db.create_all()
        test_playlist = Playlist(playlist_name = "Test Playlist")
        db.session.add(test_playlist)
        db.session.commit()

        test_song = Song(song_title = "Test Song", artist_name= "Test Artist", genre= "Test Genre", release_year= 2021, playlist=1)
        db.session.add(test_song)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'),
        follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
    
    def test_view_playlist_get(self):
        response = self.client.get(url_for('view_playlist', playlist_id=1),
        follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_create_playlist_get(self):
        response = self.client.get(url_for('create_playlist'),
        follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_addsong_get(self):
        response = self.client.get(url_for('addsong'),
        follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update', playlist_id=1),
        follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

    def test_deletesong(self):
        response = self.client.get(url_for('deletesong', song_id=1),
        follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
    
    def test_delete_get(self):
        response = self.client.get(url_for('delete', playlist_id=1),
        follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_view_playlist(self):
        response = self.client.get(url_for('home'),
        follow_redirects=True
        )
        self.assertNotIn(b"Test the Flask app", response.data)

class TestAdd(TestBase):
    def test_create_playlist(self):
        response = self.client.post(url_for('create_playlist'),
        data = dict(playlist_name= "Rock"), 
        follow_redirects=True
        )
        self.assertIn(b"Rock", response.data)
    
    def test_addsong(self):
        response = self.client.post(url_for('addsong'),
        data = dict(song_title= "Smells Like Teen Spirit", artist_name= "Nirvana", genre= "Rock", release_year= 1991, playlist=1), 
        follow_redirects=True
        )
        self.assertIn(b"Smells Like Teen Spirit", response.data)
        self.assertIn(b"Nirvana", response.data)
        self.assertIn(b"Rock", response.data)
        self.assertIn(b"1991", response.data)
        self.assertIn(b"1", response.data)

class TestUpdate(TestBase):
    def test_update(self):
        response = self.client.post(url_for('update', playlist_id=1), 
        data = dict(playlist_name="Updated Playlist"),
        follow_redirects=True
        )
        self.assertIn(b"Updated Playlist", response.data)

class TestDelete(TestBase):
    def test_delete(self):
        response = self.client.post(url_for('delete', playlist_id=1),
        follow_redirects=True
        )
        self.assertNotIn(b"Test Playlist", response.data)
    
    def test_deletesong(self):
        response = self.client.post(url_for('deletesong', song_id=1),
        follow_redirects=True
        )
        self.assertNotIn(b"Test Song", response.data)