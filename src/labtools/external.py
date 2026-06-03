from datetime import datetime


def current_year():
    return datetime.now().year


def get_profile(user_id, client):
    data = client.get_user(user_id)
    return {"id": user_id, "name": data["name"]}
