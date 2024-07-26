from flask import Blueprint, jsonify, request
from app.models import Retreats
from sqlalchemy import or_

main = Blueprint('main', __name__)


@main.route('/retreats', methods=['GET'])
def get_retreats():
    # Get query parameters with default values
    filter_term = request.args.get('filter', '')
    location = request.args.get('location', '')
    search_term = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 100))

    # Print for debugging
    print(f'filter_term{filter_term}', f'location{location}',
          f'search_term{search_term}', page, limit)

    # Build query
    query = Retreats.query

    if filter_term:
        query = query.filter(
            or_(
                Retreats.title.ilike(f'%{filter_term}%'),
                Retreats.description.ilike(f'%{filter_term}%'),
                Retreats.condition.ilike(f'%{filter_term}%'),
                Retreats.type.ilike(f'%{filter_term}%'),
                Retreats.tag.any(filter_term)  # Assumes tag is an array
            )
        )

    if location:
        query = query.filter(Retreats.location.ilike(f'%{location}%'))

    if search_term:
        query = query.filter(Retreats.title.ilike(f'%{search_term}%'))

    # Apply pagination
    total = query.count()
    retreats = query.offset((page - 1) * limit).limit(limit).all()

    return jsonify({
        'total': total,
        'pages': (total // limit) + (1 if total % limit else 0),
        'current_page': page,
        'per_page': limit,
        'retreats': [retreat.to_dict() for retreat in retreats]
    })
