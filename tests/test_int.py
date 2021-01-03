import unittest
import time
from flask import url_for
from urllib.request import urlopen

from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Playlist, Song

class TestBase(LiveServerTestCase):
    
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
        app.config['SECRET_KEY'] = 'TEST_SECRET_KEY'
        return app

    def setUp(self):
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/user/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.drop_all()
        db.create_all()

        test_playlist = Playlist(playlist_name = "Test Playlist")
        db.session.add(test_playlist)
        db.session.commit()
        
    def tearDown(self):
            # Stops the driver after each test
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestPlaylistCreation(TestBase):
    def test_playlist_creation(self):
        """
        Test that a user can navigate to the Create Task page,
        enter the description for the task and check to see if
        it redirects to the home page
        """

        # Navigate to the Create Task page
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        time.sleep(1)

        # Input the task description into the form field
        self.driver.find_element_by_xpath('//*[@id="playlist_name"]').send_keys('Integration Playlist')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to home page
        assert url_for('home') in self.driver.current_url
        assert Playlist.query.filter_by(playlist_id=1).first().playlist_name=="Integration Playlist"

if __name__ == '__main__':
    unittest.main(port=5000)