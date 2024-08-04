import pygame
from musicplayer import play_music,stop_music,pause_music,unpause_music,setvolumelevel
import time
from flask import Blueprint, jsonify

app_music = Blueprint('music', __name__)

music_library = [
    {'id': 1, 'title': 'bling', 'artist': 'Unknown'},
    {'id': 2, 'title': 'lamba', 'artist': 'unknown'},
]


@app_music.route('/library',methods=['GET'])
def getmusiclibrary():
    return jsonify({"music_library": music_library })


@app_music.route('/library/<id>',methods=['GET'])
def getmusic(id):
    for music in music_library:
        if music['id']==int(id):
            return jsonify({"music": music })
    return jsonify({"message": "notfound" })

@app_music.route('/play/<id>',methods=['POST'])
def play_sound(id):
    play_music("./songs/"+str(id)+".mp3")
    return jsonify({"message": "Music playing"})


@app_music.route('/pause',methods=['POST'])
def pause():
    pause_music()
    return jsonify({"message": "Music paused"})


@app_music.route('/unpause',methods=['POST'])
def unpause():
    unpause_music()
    return jsonify({"message": "Music continued"})


@app_music.route('/stop',methods=['POST'])
def stop():
    stop_music()
    return jsonify({"message": "Music Stopped"})

