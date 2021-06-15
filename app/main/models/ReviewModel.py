from datetime import datetime
from . import db
from marshmallow import Schema

class ReviewModel(db.Model):
	# Review Table Model
	__tablename__ = "reviews"

	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	review_time = db.Column(db.String())
	reviewer_name = db.Column(db.String())
	rating = db.Column(db.Integer)
	review_text = db.Column(db.String)
	created_at = db.Column(db.DateTime)
	modified_at = db.Column(db.DateTime)

	def serialize(self):
		return {"id": self.id,"review_time": self.review_time,"reviewer_name": self.reviewer_name, "rating": self.rating, "review_text": self.review_text}

	# class constructor
	def __init__(self, review_time, reviewer_name, rating, review_text):
		self.review_time = review_time
		self.reviewer_name = reviewer_name
		self.rating = rating
		self.review_text = review_text
		self.created_at = datetime.utcnow()
		self.modified_at = datetime.utcnow()
	
	def __repr__(self):
		  return '%s/%s/%s/%s/%s' % (self.id, self.review_time, self.reviewer_name, self.rating, self.review_text)
	
	# Save to DB
	def save(self):
		db.session.add(self)
		db.session.commit()
	
	# Update review
	def update(self, data):
		for key, item in data.items():
			setattr(self, key, item)
		self.modified_at = datetime.utcnow()
		db.session.commit()
	
	# Delete review
	def delete(self):
		db.session.delete(self)
		db.session.commit()
	
	# Get All Reviewes
	@staticmethod
	def get_all_reveiws():
		return ReviewModel.query.all()
	
	# Get Review By ID
	@staticmethod
	def get_review_by_id(id):
		return ReviewModel.query.get(id)


class ReviewSchema(Schema):
	class Meta:fields = ('id', 'review_time', 'reviewer_name', 'rating', 'review_text', 'created_at','modified_at')