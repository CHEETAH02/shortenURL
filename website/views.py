from flask import Blueprint, render_template, request, jsonify, redirect
from .database import db
import string
import random

views = Blueprint('views', __name__)
urls = db['urls']


@views.route('/')
def index():
    return render_template('welcome.html')


@views.route('/shorten-and-check-url', methods=['POST'])
def shorten_and_check_url():
    data = request.get_json()
    original_url = data['oldURL']
    base_url = data['baseURL']

    shortened_url = base_url + '/' + \
        ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    while urls.find_one({"shortenedURL": shortened_url}):
        shortened_url = base_url + '/' + \
            ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    dict = {
        "originalURL": original_url,
        "shortenedURL": shortened_url,
    }
    urls.insert_one(dict)
    return jsonify({"shortenedURL": shortened_url})


@views.route('/<path>')
def check_path_and_reroute(path):
    url = request.host + '/' + path
    if urls.find_one({"shortenedURL": url}):
        original_url = urls.find_one({"shortenedURL": url})['originalURL']
        return redirect(original_url)
    return '', 404
