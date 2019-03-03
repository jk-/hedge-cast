import jwt
import json

from flask import Blueprint, request, jsonify
from app.repository.playlist_repository import PlaylistRepository
from app.models.playlist import Playlist
from app.util.serialize import serialize
from app.util.token_required import token_required
from app.util.dotdict import dotdict
from app.validator.playlist import PlaylistValidator

playlist_blueprint = Blueprint("playlists", __name__)


@playlist_blueprint.route("/playlists", methods=("GET",))
@token_required
def get_playlists(*args, **kwargs):
    playlists = PlaylistRepository.query.all()
    return jsonify(serialize(playlists)), 200


@playlist_blueprint.route("/playlist/<int:playlist_id>", methods=("GET",))
@token_required
def get_playlist(playlist_id, *args, **kwargs):
    playlist = PlaylistRepository.query.get(playlist_id)
    return jsonify(serialize(playlist)), 200


@playlist_blueprint.route("/playlist", methods=("POST",))
@token_required
def save_playlist(*args, **kwargs):
    data = request.get_json()
    validator = PlaylistValidator(**data, csrf_enabled=False)

    if not validator.validate():
        raise Exception(validator.errors)

    data = dotdict(data)
    if not data.id:
        playlist = Playlist()
    else:
        playlist = PlaylistRepository.get(data.id)
    playlist.update(**data)
    PlaylistRepository.save(playlist)
    return jsonify(serialize(playlist)), 201


@playlist_blueprint.route("/playlist/<int:playlist_id>", methods=("DELETE",))
@token_required
def delete_playlist(playlist_id, *args, **kwargs):
    playlist = PlaylistRepository.query.get(playlist_id)
    if playlist:
        PlaylistRepository.delete(playlist)
    return jsonify({"message": "Playlist deleted.", "type": "success"}), 200
