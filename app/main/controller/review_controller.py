from flask import request, Blueprint, Response, json
from ..models.ReviewModel import ReviewModel, ReviewSchema

review_api = Blueprint('review_api', __name__)
# Init schema
review_schema = ReviewSchema()

@review_api.route('/', methods=['POST'])
def create():
	req_data = request.get_json()
	data = review_schema.load(req_data)
	review = ReviewModel(review_time=data['review_time'],reviewer_name=data['reviewer_name'],rating=data['rating'],review_text=data['review_text'])
	review.save()
	created_review = review_schema.dump(review)
	return response_warpper(created_review, 200)

@review_api.route('/', methods=['GET'])
def get_all():
	reviews = ReviewModel.get_all_reveiws()
	reviews_data = review_schema.dump(reviews, many=True)
	return response_warpper(reviews_data, 200)

@review_api.route('/<int:id>', methods=['GET'])
def get_by_id(id):
	review = ReviewModel.get_review_by_id(id)
	if not review:
		return response_warpper({'error': 'Review not found'}, 404)
	review_data = review_schema.dump(review)
	return response_warpper(review_data, 200)

@review_api.route('/<int:id>', methods=['PUT'])
def update(id):
	req_data = request.get_json()
	print(req_data)
	data = review_schema.load(req_data, partial=True)
	review = ReviewModel.get_review_by_id(id)
	if not review:
		return response_warpper({'error': 'Review not found'}, 404)
	print(data)
	review.update(data)
	updated_review = review_schema.dump(review)
	return response_warpper(updated_review, 200)

@review_api.route('/<int:id>', methods=['DELETE'])
def delete(id):
	review = ReviewModel.get_review_by_id(id)
	if not review:
		return response_warpper({'error': 'Review not found'}, 404)
	review.delete()
	return response_warpper({'message': 'deleted'}, 200)

def response_warpper(res, status_code):
	return Response(mimetype="application/json", response=json.dumps(res),status=status_code)
