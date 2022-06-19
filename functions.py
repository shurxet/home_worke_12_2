import json

POST_PATH = "posts.json"

def post_load():
    with open(POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts

def post_upload(post):
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(post, file, indent=4, ensure_ascii=False)

