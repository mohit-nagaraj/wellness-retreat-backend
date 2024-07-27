from sqlalchemy import or_
from datetime import datetime
from flask import Blueprint, jsonify, request

from . import db
from app.models.retreats import Retreats
from app.models.bookings import Bookings

main = Blueprint('main', __name__)


@main.route('/api/retreats', methods=['GET'])
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


@main.route('/api/book', methods=['POST'])
def book_retreat():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    for field in ['user_id', 'user_name', 'user_email', 'user_phone', 'retreat_id', 'retreat_title', 'retreat_location', 'retreat_price', 'retreat_duration', 'payment_details', 'booking_date']:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Check if the user has already booked the retreat
    existing_booking = Bookings.query.filter_by(
        user_id=data['user_id'], retreat_id=data['retreat_id']).first()
    if existing_booking:
        return jsonify({"error": "User has already booked this retreat"}), 400

    try:
        new_booking = Bookings(
            user_id=data['user_id'],
            user_name=data['user_name'],
            user_email=data['user_email'],
            user_phone=data['user_phone'],
            retreat_id=data['retreat_id'],
            retreat_title=data['retreat_title'],
            retreat_location=data['retreat_location'],
            retreat_price=data['retreat_price'],
            retreat_duration=data['retreat_duration'],
            payment_details=data['payment_details'],
            booking_date=datetime.fromisoformat(data['booking_date'])
        )
        db.session.add(new_booking)
        db.session.commit()
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    return jsonify(new_booking.to_dict()), 201
