from flask import Flask, render_template, url_for, redirect 
from .main.models import db, ReviewModel
from .main.util.scrap import fetchGoogleReview
from .config import app_config
from .main.controller.review_controller import review_api as review_blueprint
from flask_graphql import GraphQLView
from app.main.schemas.schema_review import schema

app = Flask(__name__,template_folder='../templates',static_folder='../static')

@app.route('/')
def index():
    return redirect(url_for('allReviews'))

@app.route('/reviews')
def getReviews():
    scarp_data = fetchGoogleReview()
    for reviews in scarp_data:
        review_model = ReviewModel(review_time=reviews['review_time'],reviewer_name=reviews['reviewer_name'],rating=reviews['rating'],review_text=reviews['review_text'])
        review_model.save()
    return redirect(url_for('allReviews'))

@app.route('/home')
def allReviews():
    scarp_data = ReviewModel.get_all_reveiws() 
    return render_template("home.html", data=scarp_data)

def create_app(env_name):
    app.config.from_object(app_config[env_name])
    db.init_app(app)
    app.register_blueprint(review_blueprint, url_prefix='/api/v1/reviews')
    app.add_url_rule('/graphql-api',view_func=GraphQLView.as_view('graphql',schema=schema,graphiql=True))
    return app