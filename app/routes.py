from flask import Blueprint, jsonify
from app.models import Retreats

main = Blueprint('main', __name__)


@main.route('/retreats', methods=['GET'])
def get_retreats():
    retreats = Retreats.query.all()

    return jsonify([retreat.to_dict() for retreat in retreats])
