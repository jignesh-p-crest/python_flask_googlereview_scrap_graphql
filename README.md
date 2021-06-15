# Python Flask google Review Scraping
A simple scraper to extract all Google reviews for the business

- Create Virtual Environment and install dependencies

```
> virtualenv venv
> source venv/Scripts/activate
> pip install -r requirements.txt
```
- DB migration 
```
> python manage.py db init

> python manage.py db migrate

> python manage.py db upgrade
```
- Run application
```
> python run.py
```

- Viewing the app
```
> Open the following url on your browser: http://127.0.0.1:5000/
```
![image](https://raw.github.com/jignesh-p-crest/python_flask_googlereview_scrap/master/static/web_page.PNG)


- To run unit test
```
> python test.py

```

- RESTful API Endpoints for reviews
  - To get all reviews : GET - /api/v1/reviews
  - To get review details: GET - /api/v1/reviews/<id>  
  - To create new review: POST - /api/v1/reviews/
      ```
       {
        "rating": 3,
        "review_text": "The Review Text",
        "review_time": "a week ago",
        "reviewer_name": "Test Reviewr"
      }
    ```
  - To update review: PUT -  /api/v1/reviews/<id>
     ```
       {
        "rating": 4,
        "review_text": "The Review Text for update",
        "review_time": "a day ago",
        "reviewer_name": "Test Reviewr"
      }
    ```
  - To delete the review DELETE: /api/v1/reviews/<id>

- GraphQL API endpoint: http://127.0.0.1:5000/graphql-api
    - To get all reviews :
    ![image](https://raw.github.com/jignesh-p-crest/python_flask_googlereview_scrap/master/static/reviews.PNG)

    - To get review by Id :
    ![image](https://raw.github.com/jignesh-p-crest/python_flask_googlereview_scrap/master/static/reviews_by_id.PNG)

    - To create new review :
    ![image](https://raw.github.com/jignesh-p-crest/python_flask_googlereview_scrap/master/static/create_review.PNG)

    - To get update review :
    ![image](https://raw.github.com/jignesh-p-crest/python_flask_googlereview_scrap/master/static/update_reveiw.PNG)

    - To get delete review :
    ![image](https://raw.github.com/jignesh-p-crest/python_flask_googlereview_scrap/master/static/delete_review.PNG)