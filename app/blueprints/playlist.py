from flask import Blueprint, request, jsonify
from app.repository.playlist_repository import PlaylistRepository
from app.repository.category_repository import CategoryRepository
from app.models.playlist import Playlist
from app.util.serialize import serialize
from app.util.token_required import token_required
from app.util.dotdict import dotdict
from app.validator.playlist import PlaylistValidator

playlist_blueprint = Blueprint("playlists", __name__)


@playlist_blueprint.route("/playlists", methods=("GET",))
def get_playlists(*args, **kwargs):
    playlists = PlaylistRepository.query.all()
    return jsonify(serialize(playlists)), 200


@playlist_blueprint.route("/playlist/<int:playlist_id>", methods=("GET",))
def get_playlist(playlist_id, *args, **kwargs):
    playlist = PlaylistRepository.query.get(playlist_id)
    return jsonify(serialize(playlist)), 200


admin_playlist_blueprint = Blueprint("admin_playlist", __name__)


@admin_playlist_blueprint.before_request
@token_required(roles=["ROLE_ADMIN"])
def before_request(*args, **kwargs):
    """ Protect all of the admin endpoints. """
    pass


@admin_playlist_blueprint.route("/playlist", methods=("POST",))
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

    playlist.categories = []
    print(data.categories)

    for category in data.categories:
        _cat = CategoryRepository.get_by_name(category)
        playlist.categories.append(_cat)

    PlaylistRepository.save(playlist)
    return jsonify(serialize(playlist)), 201


@admin_playlist_blueprint.route(
    "/playlist/<int:playlist_id>", methods=("DELETE",)
)
def delete_playlist(playlist_id, *args, **kwargs):
    playlist = PlaylistRepository.query.get(playlist_id)
    if playlist:
        PlaylistRepository.delete(playlist)
    return jsonify({"message": "Playlist deleted.", "type": "success"}), 200
