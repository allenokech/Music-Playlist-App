from application import app, db
from application.models import Song, Playlist, association_table
from application.forms import TaskForm
from flask import render_template, request, redirect, url_for