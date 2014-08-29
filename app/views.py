# coding: utf-8
from app import app
from app.front import frontView
from flask import redirect, url_for

app.register_blueprint(frontView, url_prefix='/main')


@app.route('/')
def index():
    return redirect(url_for('front.index'))
