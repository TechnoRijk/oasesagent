from celery import Celery
from . import create_app, db
from .models import LinkedInPost
import os

def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    return celery

app = create_app()
celery = make_celery(app)

@celery.task
def schedule_post(post_id):
    with app.app_context():
        post = LinkedInPost.query.get(post_id)
        if post:
            # Logic to post to LinkedIn using LinkedIn API
            pass
