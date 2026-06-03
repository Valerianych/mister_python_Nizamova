import os


def get_mode():
    return os.environ.get("APP_MODE", "dev")


def build_url(host):
    mode = get_mode()
    return f"https://{host}/{mode}"
