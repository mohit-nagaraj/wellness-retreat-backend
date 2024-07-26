from . import db


class Retreats(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(50), nullable=True)
    condition = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    tag = db.Column(db.ARRAY(db.String), nullable=True)
    duration = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'date': int(self.date.timestamp()) if self.date else None,
            'location': self.location,
            'price': self.price,
            'type': self.type,
            'condition': self.condition,
            'image': self.image,
            'tag': self.tag,
            'duration': self.duration
        }
