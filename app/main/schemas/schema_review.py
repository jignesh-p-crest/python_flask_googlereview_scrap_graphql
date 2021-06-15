from datetime import datetime
from app.main.models.ReviewModel import ReviewModel, db
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.main.util.helper import input_to_dictionary

class ReviewAttribute:
	id=graphene.Int()
	review_time = graphene.String()
	reviewer_name = graphene.String()
	rating = graphene.Int()
	review_text = graphene.String()
	created_at = graphene.DateTime()
	modified_at = graphene.DateTime()

class Review(SQLAlchemyObjectType):
	class Meta:
		model = ReviewModel
		interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
	node = graphene.relay.Node.Field()
	reviews = SQLAlchemyConnectionField(Review)

	review = graphene.Field(Review, id=graphene.Int())

	def resolve_review(root, info, id):
		review = ReviewModel.query.get(id)
		return review

class CreateReviewInput(graphene.InputObjectType, ReviewAttribute):
	"""Arguments to create a review."""
	pass

class CreateReview(graphene.Mutation):
	review = graphene.Field(lambda: Review, description="Review created by this mutation.")
	
	class Arguments:
		review = CreateReviewInput(required=True)
		
	def mutate(self, info, review):
		data = input_to_dictionary(review)
		review = ReviewModel(**data)
		review.save()

		return CreateReview(review=review)

class UpdateReviewInput(graphene.InputObjectType, ReviewAttribute):
	"""Arguments to update a review."""
	pass

class UpdateReview(graphene.Mutation):
	review = graphene.Field(lambda: Review, description="Review updated by this mutation.")
	id = graphene.Int()

	class Arguments:
		id = graphene.Int()
		review = UpdateReviewInput(required=True)
	
	def mutate(self, info, id, review):
		data = input_to_dictionary(review)

		review = ReviewModel.query.get(id)
		review.update(data)
		
		review = ReviewModel.query.get(id)

		return UpdateReview(review=review)

class DeleteReview(graphene.Mutation):
	review = graphene.Field(lambda: Review, description="Review updated by this mutation.")
	id = graphene.Int()

	class Arguments:
		id = graphene.Int()
	
	def mutate(self, info, id):
		review = ReviewModel.query.get(id)
		review.delete()
		return DeleteReview(review=review)

class Mutation(graphene.ObjectType):
	createReview = CreateReview.Field()
	updateReview = UpdateReview.Field()
	deleteReview = DeleteReview.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)