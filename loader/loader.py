from flask import Blueprint, request, render_template
from functions import post_load, post_upload
import logging

logging.basicConfig(encoding='utf-8', level=logging.INFO)

loader_blueprint = Blueprint('loader', __name__, url_prefix='/post', static_folder='static',template_folder='templates')

@loader_blueprint.route('/form/')
def loader():
    return render_template('post_form.html')

@loader_blueprint.route('/upload/', methods=["POST"])
def upload():
    try:
        file = request.files['picture']
        filename = file.filename
        content = request.values['content']
        post = post_load()
        post.append({
            'pic': f'/uploads/images/{filename}',
            'content': content
        })
        post_upload(post)
        file.save(f'uploads/images/{filename}')
        if filename.split('.')[-1] not in ['jpeg', 'jpg', 'png']:
            logging.info(f'Файл {filename} не изображение')
    except FileNotFoundError:
        logging.error('Ошибка при загрузкe файла')
        return "<h1> Файл не найден </h1>"
    else:
        return render_template('post_uploaded.html', pic=f'/uploads/images/{filename}', content=content)




