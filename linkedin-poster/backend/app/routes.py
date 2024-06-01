from flask import Blueprint, request, jsonify
from .models import LinkedInPost, Company, db
from .tasks import schedule_post
from .utils import generate_image, generate_text

main = Blueprint('main', __name__)

@main.route('/api/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    content = generate_text(data['content'])
    image_url = generate_image(data['image_prompt'])
    scheduled_time = data['scheduled_time']

    post = LinkedInPost(content=content, image_url=image_url, scheduled_time=scheduled_time)
    db.session.add(post)
    db.session.commit()

    schedule_post.apply_async((post.id,), eta=scheduled_time)

    return jsonify({'message': 'Post scheduled successfully!'})
