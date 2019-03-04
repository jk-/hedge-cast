from flask import Blueprint, request, jsonify
from app.repository.video_repository import VideoRepository
from app.models.video import Video
from app.util.serialize import serialize
from app.util.token_required import token_required
from app.util.dotdict import dotdict
from app.validator.video import VideoValidator

videos_blueprint = Blueprint("videos", __name__)


@videos_blueprint.route("/videos", methods=("GET",))
def get_videos(*args, **kwargs):
    videos = VideoRepository.query.all()
    return jsonify(serialize(videos)), 200


@videos_blueprint.route("/video/<int:video_id>", methods=("GET",))
def get_video(video_id, *args, **kwargs):
    video = VideoRepository.query.get(video_id)
    return jsonify(serialize(video)), 200


@videos_blueprint.route("/video/<search_term>", methods=("GET",))
def search_videos(search_term, *args, **kwargs):
    videos = VideoRepository.get_by_search(search_term)
    return jsonify(serialize(videos)), 200


admin_videos_blueprint = Blueprint("admin_videos", __name__)


@admin_videos_blueprint.before_request
@token_required(roles=["ROLE_ADMIN"])
def before_request(*args, **kwargs):
    """ Protect all of the admin endpoints. """
    pass


@admin_videos_blueprint.route("/video", methods=("POST",))
def save_video(*args, **kwargs):
    data = request.get_json()
    validator = VideoValidator(**data, csrf_enabled=False)

    if not validator.validate():
        raise Exception(validator.errors)

    data = dotdict(data)
    if not data.id:
        video = Video()
    else:
        video = VideoRepository.get(data.id)
    video.update(**data)
    VideoRepository.save(video)
    return jsonify(serialize(video)), 201


@admin_videos_blueprint.route("/video/<int:video_id>", methods=("DELETE",))
def delete_video(video_id, *args, **kwargs):
    video = VideoRepository.query.get(video_id)
    if video:
        VideoRepository.delete(video)
    return jsonify({"message": "Video deleted.", "type": "success"}), 200
