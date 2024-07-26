from app import db
from datetime import datetime


class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False)
    user_phone = db.Column(db.String(15), nullable=False)
    retreat_id = db.Column(db.String(255), nullable=False)
    retreat_title = db.Column(db.String(255), nullable=False)
    retreat_location = db.Column(db.String(255), nullable=False)
    retreat_price = db.Column(db.Float, nullable=False)
    retreat_duration = db.Column(db.Integer, nullable=False)
    payment_details = db.Column(db.JSON, nullable=False)
    booking_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    db.UniqueConstraint('user_id', 'retreat_id', name='unique_booking')

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'user_name': self.user_name,
            'user_email': self.user_email,
            'user_phone': self.user_phone,
            'retreat_id': self.retreat_id,
            'retreat_title': self.retreat_title,
            'retreat_location': self.retreat_location,
            'retreat_price': self.retreat_price,
            'retreat_duration': self.retreat_duration,
            'payment_details': self.payment_details,
            'booking_date': self.booking_date.isoformat()
        }
