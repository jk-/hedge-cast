from flask import Blueprint, request, jsonify
from app.repository.playlist_repository import PlaylistRepository
from app.repository.category_repository import CategoryRepository
from app.repository.video_playlist_repository import VideoPlaylistRepository
from app.repository.video_repository import VideoRepository
from app.models.video import Video
from app.models.video_playlist import VideoPlaylist
from app.models.playlist import Playlist
from app.util.serialize import serialize
from app.util.token_required import token_required
from app.util.dotdict import dotdict
from app.validator.playlist import PlaylistValidator

playlist_blueprint = Blueprint("playlists", __name__)


@playlist_blueprint.route("/playlists", methods=("GET",))
def get_playlists(*args, **kwargs):
    playlists = PlaylistRepository.all()
    return jsonify(serialize(playlists)), 200


@playlist_blueprint.route("/playlist/<int:playlist_id>", methods=("GET",))
def get_playlist(playlist_id, *args, **kwargs):
    playlist = PlaylistRepository.get(playlist_id)
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

    for category in data.categories:
        _cat = CategoryRepository.first(name=category)
        playlist.categories.append(_cat)

    PlaylistRepository.save(playlist)

    playlist.videos = []

    for key, video_id in enumerate(data.videos):
        video = VideoRepository.get(video_id)
        video_playlist = VideoPlaylist(
            playlist=playlist, video=video, order_by=key
        )
        VideoPlaylistRepository.save(video_playlist)
    return jsonify(serialize(playlist)), 201


@admin_playlist_blueprint.route(
    "/playlist/<int:playlist_id>", methods=("DELETE",)
)
def delete_playlist(playlist_id, *args, **kwargs):
    playlist = PlaylistRepository.get(playlist_id)
    if playlist:
        PlaylistRepository.delete(playlist)
    return jsonify({"message": "Playlist deleted.", "type": "success"}), 200
