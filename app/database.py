from . import db


def setup_db(app):
    with app.app_context():
        db.create_all()
