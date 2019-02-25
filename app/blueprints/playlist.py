import jwt
import json

from flask import Blueprint, request, jsonify
from app.repository.playlist_repository import PlaylistRepository
from app.models.playlist import Playlist
from app.service.serialize import serialize
from app.token_required import token_required

playlist_blueprint = Blueprint("playlists", __name__)


@playlist_blueprint.route("/playlists", methods=("GET",))
@token_required
def get_users(*args, **kwargs):
    playlists = PlaylistRepository.query.all()
    return jsonify(serialize(playlists)), 201


@playlist_blueprint.route("/playlist/<int:playlist_id>", methods=("GET",))
@token_required
def get_user(playlist_id, *args, **kwargs):
    playlist = PlaylistRepository.query.get(playlist_id)
    return jsonify(serialize(playlist)), 201
