import jwt
import json

from flask import Blueprint, request, jsonify
from app.repository.video_repository import VideoRepository
from app.models.video import Video
from app.service.serialize import serialize
from app.token_required import token_required
from app.service.dotdict import dotdict

videos_blueprint = Blueprint("videos", __name__)


@videos_blueprint.route("/videos", methods=("GET",))
@token_required
def get_videos(*args, **kwargs):
    videos = VideoRepository.query.all()
    return jsonify(serialize(videos)), 200


@videos_blueprint.route("/video/<int:video_id>", methods=("GET",))
@token_required
def get_video(video_id, *args, **kwargs):
    video = VideoRepository.query.get(video_id)
    return jsonify(serialize(video)), 200


@videos_blueprint.route("/video", methods=("POST",))
@token_required
def save_video(*args, **kwargs):
    data = dotdict(request.get_json())
    if not data.id:
        video = Video()
    else:
        video = VideoRepository.get(data.id)
    video.update(**data)
    VideoRepository.save(video)
    return jsonify(serialize(video)), 201


@videos_blueprint.route("/video/<int:video_id>", methods=("DELETE",))
@token_required
def delete_video(video_id, *args, **kwargs):
    video = VideoRepository.query.get(video_id)
    if video:
        VideoRepository.delete(video)
    return jsonify({"message": "Video deleted.", "type": "success"}), 200
