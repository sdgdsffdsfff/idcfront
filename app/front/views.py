# coding: utf-8
from flask import render_template,  Blueprint

frontView = Blueprint('front', __name__, template_folder='./templates',
    static_folder='./static')

@frontView.route('/')
def index():
    return render_template('pages/main.html')


@frontView.route('/service')
def service():
    return render_template('pages/service.html')


@frontView.route('/room')
def room():
    return render_template('pages/room.html',
    web_3d_url="http://110.249.213.19:8080/uinv_demo/index.html?user=admin&pwd=123&type=3d")