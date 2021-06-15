from flask_sqlalchemy import SQLAlchemy

# initialize our db
db = SQLAlchemy()

from .ReviewModel import ReviewModel, ReviewSchema