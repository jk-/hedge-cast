import jwt
import json

from flask import Blueprint, request, jsonify
from app.repository.video_repository import VideoRepository
from app.models.video import Video
from app.service.serialize import serialize
from app.token_required import token_required

videos_blueprint = Blueprint("videos", __name__)


@videos_blueprint.route("/videos", methods=("GET",))
@token_required
def get_videos(*args, **kwargs):
    videos = VideoRepository.query.all()
    return jsonify(serialize(videos)), 201


@videos_blueprint.route("/video/<int:video_id>", methods=("GET",))
@token_required
def get_video(video_id, *args, **kwargs):
    video = VideoRepository.query.get(video_id)
    return jsonify(serialize(video)), 201
